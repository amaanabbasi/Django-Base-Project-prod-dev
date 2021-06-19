# Django Base Project separating development and production workflow.

# Directory structure

Delete settings.py & wsgi.py, these will have two different files for development and production.

```
 settings
    |- base.py  // few things will be common for both development and production
    |- dev.py
    |- prod.py

 wsgi
   |- dev.py
   |- prod.py
```  

to run development

`python manage-dev.py runserver`


to run in production mode this will be different, as on a server the application should keep running in the background. Below I have given a example code for deploying it on apache2 server.

```

<VirtualHost *:80>
ServerAdmin email@gmail.com
DocumentRoot /home/ubuntu/mysite/
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
Alias /static /home/ubuntu/mysite/mysite/static_cdn
<Directory /home/ubuntu/mysite/mysite/static_cdn>
Require all granted
</Directory>
<Directory /home/ubuntu/mysite/mysite/wsgi>
<Files prod.py>
Require all granted
</Files>
</Directory>
WSGIDaemonProcess mysite python-path=/home/ubuntu/mysite python-home=/home/ubuntu/venv 
WSGIProcessGroup mysite
WSGIScriptAlias / /home/ubuntu/mysite/mysite/wsgi/prod.py
WSGIPassAuthorization On
</VirtualHost>
 
```
