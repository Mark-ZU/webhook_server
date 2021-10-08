import sys
from github_webhook import Webhook
from flask import Flask

try:
    with open("hash/.zecrey.sec","rb") as f:
        _sec = f.read()
except IOError:
    print("IOERROR!!!!! no secret file")
    sys.exit(-1)

app = Flask(__name__)
webhook = Webhook(app,'/',_sec)

@webhook.hook(event_type='push')
def on_push(data):
    print("Get push with: {0}".format(data),)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4567)
