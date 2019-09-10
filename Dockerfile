FROM alpine
FROM python:3.7

RUN mkdir /srv/api -p

RUN apt-get update
RUN apt-get install python-mysqldb

ADD requirements.txt /srv/api/requirements.txt

RUN pip install -r /srv/api/requirements.txt

ADD . /srv/api/

EXPOSE 8080


CMD ["uwsgi", "--http" , ":80",  "--wsgi-file", "/srv/api/webservice/wsgi.py", "--master",  "--processes","4", "--threads", "4"]

