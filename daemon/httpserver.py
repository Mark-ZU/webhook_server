from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from hash import check
HOST_NAME = ''
PORT = 4567

class Handler(BaseHTTPRequestHandler):
    def _set_server(self):
        self.server_version = "ZecreyWebhook/0.0.1"
        self.sys_version = "ZecreyServer"
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"OK\n")
    def _set_failure(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"OK\n")
    def _set_get_res(self):
        self.send_response(500)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        self._set_get_res()
    def do_POST(self):
        self._set_server()
        self.print_sign()
        content_length = int(self.headers['Content-Length'] or 0)
        content_type = self.headers['Content-Type'] or ""
        event = self.headers['X-GitHub-Event'] or ""
        sign = self.headers['X-Hub-Signature'] or ""
        sign_256 = self.headers['X-Hub-Signature-256'] or ""
        body = self.rfile.read(content_length)
        res = check(body,sign_256)
        if not res:
            self._set_failure()
            return None
        # print("------------------body--------------\n",body)
        req,res = self.parse_json(body)
        if not res:
            self._set_failure()
            return None

        # do req here

        self._set_response()
    def print_sign(self):
        print("------------------print----------------")
        content_type = self.headers['Content-Type']
        event = self.headers['X-GitHub-Event']
        sign = self.headers['X-Hub-Signature']
        sign_256 = self.headers['X-Hub-Signature-256']
        print("Content-Type: ",content_type)
        print("X-GitHub-Event: ",event)
        print("X-Hub-Signature: ",sign)
        print("X-Hub-Signature-256: ",sign_256)

    def parse_json(self,byte_msg):
        try:
            data = json.loads(byte_msg.decode('utf-8'))
        except ValueError as e:
            return None,False
        return data,True

if __name__ == '__main__':
    server = HTTPServer((HOST_NAME,PORT), Handler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()