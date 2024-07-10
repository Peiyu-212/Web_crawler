##### Build Image
FROM python:3.12-slim-bullseye AS builder
LABEL maintainer Peiyu_Jhong

RUN echo "deb http://opensource.nchc.org.tw/debian/ bullseye main" > /etc/apt/sources.list \
  && echo "deb http://opensource.nchc.org.tw/debian/ bullseye-updates main" >> /etc/apt/sources.list \
  && echo "deb http://opensource.nchc.org.tw/debian/ bullseye-proposed-updates main" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends\
  build-essential \
  vim \
  wget \
  && apt-get purge -y --auto-remove \
  && rm -rf /var/lib/apt/lists/*

COPY ./backend /backend
COPY ./.env /.env
COPY ./backend/compose/local.txt /backend/requirements.txt

WORKDIR /backend
RUN pip install --upgrade pip
RUN pip install -r /backend/requirements.txt

COPY ./deploy/uwsgi.ini /etc/uwsgi/uwsgi.ini
RUN mkdir -p  /log \
  && chown -R www-data:www-data /log \
  && chown -R www-data:www-data /var/tmp/

COPY ./deploy/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN ln -s /usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

### COPY the uwsgi configuration file
COPY ./deploy/uwsgi.ini /etc/uwsgi/uwsgi.ini

### Port to use with TCP proxy
EXPOSE 55555

### Start uWSGI on container startup
CMD ["/usr/local/bin/uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]
