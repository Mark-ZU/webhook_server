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

    process = subprocess.Popen("mkdir -p supervisor".split(),stdout=subprocess.DEVNULL)
    process.wait()
    ini_file = "supervisor/"+configs["ini_name"]+".ini"
    open(ini_file, 'w').close()
    with open(ini_file,'w') as f:
        f.write(sv_conf.format(home,home,home,user))

    env = os.environ.copy()
    # env["MY_PASSWORD"] = configs['passwd']
    process = subprocess.Popen("sudo sh deploy.sh".split(),env=env,stdout=subprocess.DEVNULL)
    process.wait()
# write config file
# copy config file to supervisor and restart
# download or pull repository and call supervisor to restart zecrey
