import hashlib
import hmac

def check(msg,sign):
    try:
        with open(".zecrey.sec","rb") as f:
            _sec = f.read()
    except IOError:
        return False
    digest = hmac.new(_sec, msg=msg, digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(digest,sign)


if __name__ == "__main__":
    res = check("abc".encode(),"abc")
    print(res)