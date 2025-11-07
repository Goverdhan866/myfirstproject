FROM ubuntu:24.04
RUN apt-get update
RUN apt-get install nginx -y
COPY project.html /var/www/html
ENTRYPOINT ["nxinx", "-g", "daemon off;"]
