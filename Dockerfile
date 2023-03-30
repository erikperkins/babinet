FROM python:3.9-slim-bullseye
RUN useradd babinet
ENV APP=/app
WORKDIR $APP
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN mkdir -p /root/.duckdb
CMD ["uwsgi", "--ini", "uwsgi.ini"]
