FROM python:3.9-slim-bullseye
ENV APP=/app
WORKDIR $APP
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["uwsgi", "--ini", "uwsgi.ini"]
