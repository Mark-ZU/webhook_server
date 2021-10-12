import sys
import webhook_handler
from webhook_handler import Webhook
from flask import Flask
import logging

try:
    with open("hash/.zecrey.sec","rb") as f:
        _sec = f.read()
except IOError:
    print("IOERROR!!!!! no secret file")
    sys.exit(-1)

app = Flask(__name__)
webhook = Webhook(app,'/',_sec,"zecreyWebhook.log")

@webhook.hook(event_type='workflow_job')
def on_workflow_job(data):
    # print("Get: {0}".format(data))
    pass

@webhook.hook()
def on_all(data):
    res = webhook_handler.check_zecrey_sign(data)
    if res is not None:
        print("check success, need pull... ",data["head_commit"]["id"],data["repository"]["clone_url"])

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4567)
