import os, sys
import subprocess 
import yaml

sv_conf = """[program:webhook_server]
command=python3 server.py
directory={}
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile={}/supervisor.log
stderr_logfile={}/supervisor.err.log
user={}
"""

conf = """

"""

if __name__ == '__main__':
    with open("config.yaml","r") as f:
        try:
            configs = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit(-1)

    user = os.getlogin()
    home = os.getcwd()

    ini_file = configs["supervisor_ini"]
    open(ini_file, 'w').close()
    with open(ini_file,'w') as f:
        f.write(sv_conf.format(home,home,home,user))

    env = os.environ.copy()
    env["MY_PASSWORD"] = configs['passwd']
    subprocess.Popen("echo $MY_PASSWORD | sudo -Sk sh deploy.sh".split(),env=env,stdout=subprocess.DEVNULL)

# write config file
# copy config file to supervisor and restart
# download or pull repository and call supervisor to restart zecrey
