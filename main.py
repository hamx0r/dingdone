# Base application from https://www.svpino.com/running-a-python-fastapi-application-in-app-engine
# Production run command: gunicorn main:app -w 1 --log-level debug -k uvicorn.workers.UvicornWorker
# Dev run command `uvicorn main:app --reload --log-level debug`

import logging, colorlog
import logging.config
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# https://medium.com/@PhilippeGirard5/fastapi-logging-f6237b84ea64
# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
log = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project.
                                      # This will get the root logger since no logger in the configuration has this name.



@app.get("/")
async def index():
    log.debug('hi')
    return "Hello World!"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000, log_level='debug', reload=True)