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
  * `cp config_example.yaml config.yaml`
  * change `passwd`in `config.yaml` to the PASSWORD of current sudoer user
  * `python3 deploy.py`

