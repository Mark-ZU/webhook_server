import secrets
import hashlib as hl
import hmac
if __name__ == '__main__':
    sec = secrets.token_hex(20)
    with open("hash/.zecrey.sec","wb") as f:
        f.write(sec.encode())
