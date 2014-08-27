Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows:

WSGIDaemonProcess bigbrother-<target> threads=5 maximum-requests=1000 user=<user> group=staff
WSGIRestrictStdout Off

<VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/bigbrother/log/apache2/error.log"
        CustomLog "/srv/sites/bigbrother/log/apache2/access.log" common

        WSGIProcessGroup bigbrother-<target>

        Alias /media "/srv/sites/bigbrother/media/"
        Alias /static "/srv/sites/bigbrother/static/"

        WSGIScriptAlias / "/srv/sites/bigbrother/src/teamq/wsgi/wsgi_<target>.py"

</VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

[program:uwsgi-bigbrother-<target>]
user = <user>
command = /srv/sites/bigbrother/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/bigbrother/src/bigbrother/wsgi/wsgi_<target>.py
home = /srv/sites/bigbrother/env
master = true
processes = 8
harakiri = 600
autostart = true
autorestart = true
stderr_logfile = /srv/sites/bigbrother/log/uwsgi_err.log
stdout_logfile = /srv/sites/bigbrother/log/uwsgi_out.log
stopsignal = QUIT

Nginx
-----

upstream django_bigbrother_<target> {
  ip_hash;
  server 127.0.0.1:8001;
}

server {
  listen :80;
  server_name  my.domain.name;

  access_log /srv/sites/bigbrother/log/nginx-access.log;
  error_log /srv/sites/bigbrother/log/nginx-error.log;

  location /500.html {
    root /srv/sites/bigbrother/src/bigbrother/templates/;
  }
  error_page 500 502 503 504 /500.html;

  location /static/ {
    alias /srv/sites/bigbrother/static/;
    expires 30d;
  }

  location /media/ {
    alias /srv/sites/bigbrother/media/;
    expires 30d;
  }

  location / {
    uwsgi_pass django_bigbrother_<target>;
  }
}
