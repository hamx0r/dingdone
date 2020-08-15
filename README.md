dingdone
==
DingDone.info lets you know when you're order is up

Developing
--
If running a pure Firebase web app (doesn't work on most mobile browsers), run with `firebase emulators:start`

If running FastAPI with static frontend, first run Firestore emulator with `gcloud beta emulators firestore start --project test --host-port "localhost:8001"`


Deploying
--
`firebase deploy`

### Backend
https://fastapi.tiangolo.com/tutorial/debugging/
https://fastapi.tiangolo.com/advanced/templates/



### Frontend
https://classpert.com/blog/top-bootstrap-alternatives
https://materializecss.com/getting-started.html
https://www.muicss.com/docs/v1/example-layouts/blog

Phase 1: Web Page only
--
After running locally, visit http://localhost:5000 .  This is built on the Firebase App method.

Alternately, see the main.py file for a possibly Python 3 Fast API method (abandoned?)

Each order has 3 `status` phases:
1. Open - it means a customer as registered their order and the row is currently unchecked on the Business's UI
2. Ready - means order is ready for pickup.  This means Order row has been checked which causes alert to be sent to Customer
3. Closed - means order has been picked up.    


Phase 2: QR codes, image recognition
--

Phase 3: grubhub etc integration
--
