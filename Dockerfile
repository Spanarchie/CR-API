#install nginx
FROM python:3.5.1

MAINTAINER Ric Colin Moore-Hill <spanarchian@gmail.com>

# install nginx and supervisor

RUN apt-get update && \
    apt-get install -y nginx supervisor

COPY . /project

WORKDIR /project

RUN pip install -r requirements.txt

# Set up configuration files
ADD /docker_config/supervisor_app.conf /etc/supervisor/supervisord.conf
ADD /docker_config/nginx_app.conf /etc/nginx/nginx.conf


EXPOSE 80

CMD ["supervisord", "-n"]

