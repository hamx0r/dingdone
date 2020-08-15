# Base application from https://www.svpino.com/running-a-python-fastapi-application-in-app-engine
# Production run command: gunicorn main:app -w 1 --log-level debug -k uvicorn.workers.UvicornWorker
# Dev run command `uvicorn main:app --reload --log-level debug`

import logging, colorlog
import logging.config
from typing import Optional
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from google.cloud import firestore
import google.auth.credentials
from pydantic import BaseModel
import os
import mock

app = FastAPI()

# Set up FireStore credentials
if os.getenv('GAE_ENV', '').startswith('standard'):
    # production
    db = firestore.Client()
else:
    # localhost
    os.environ["FIRESTORE_DATASET"] = "test"
    os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8001"
    os.environ["FIRESTORE_EMULATOR_HOST_PATH"] = "localhost:8001/firestore"
    os.environ["FIRESTORE_HOST"] = "http://localhost:8001"
    os.environ["FIRESTORE_PROJECT_ID"] = "test"

    credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    db = firestore.Client(project="test", credentials=credentials)

class Order(BaseModel):
    business: str
    name: Optional[str] = None
    number: int

# https://medium.com/@PhilippeGirard5/fastapi-logging-f6237b84ea64
# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
log = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project.
                                      # This will get the root logger since no logger in the configuration has this name.

orders_ref = db.collection('orders')
businesses_ref = db.collection('businesses')


@app.get("/")
async def index():
    log.debug('hi')
    return "Hello World!"

@app.post("/orders/")
async def new_order(order: Order):
    log.debug(f"Order: {order.dict()}")
    update_time, doc_ref = orders_ref.add(order.dict())

    return {'status': 'success'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000, log_level='debug', reload=True)