# test cicd github
![workflow status icon](https://github.com/zjumark/try_github_action/actions/workflows/try-golang.yml/badge.svg)

* todo list
    * [x] add webhook
    * [ ] add webhook to actions
    * [ ] golang CD
    * [ ] golang with docker

---
* steps
  * install supervisor to your server
  * clone this repository to one directory
  * `cd daemon`
  * `python3 generate_secrets.py` to generate your own secret token.
  * config github : set two ENV VARIABLE in settings/secrets
    * set ZECREY_WEBHOOK_URL to http://your_server_ip_or_url:port
    * set ZECREY_WEBHOOK_SECRET as the file `daemon/hash/.zecrey.sec` stored
  * `cp config_example.yaml config.yaml`
  * change `passwd`in `config.yaml` to the PASSWORD of current sudoer user
  * `python3 deploy.py`

