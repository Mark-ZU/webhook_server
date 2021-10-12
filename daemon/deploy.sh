cp supervisor/*.ini /etc/supervisor/conf.d/ 
supervisorctl reread
supervisorctl update
service supervisor restart
# echo $MY_PASSWORD | sudo -Sk supervisorctl update


