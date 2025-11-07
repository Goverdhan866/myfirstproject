From ubuntu:24.04
Run apt-get update
Run apt-get install nginx -y
copy project.html /var/www/html
ENTRYPOINT ["nxinx", "-g", "daemon off;"]
