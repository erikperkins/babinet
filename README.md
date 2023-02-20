[![Build Status](http://52.89.207.216/jenkins/buildStatus/icon?job=github%2Fdockholliday%2Fmaster)](http://52.89.207.216/jenkins/job/github/job/dockholliday/job/master/)
## Dockholliday

This is a simple containerized Flask application.

### Build
```
$ docker build --tag dockholliday .
```

### Persist
```
$ docker volume create daisy
```

### Bind
```
-- mount type=bind,src=$(pwd),target=/src
```

### Network
```
$ docker network create kate
```

### Database
```
$ docker run \
    --detach
    --network kate \
    --network-alias tombstone \
    --volume daisy:/var/lib/postgresql/data \
    --env POSTGRES_PASSWORD=aneducatedman \
    --name tombstone \
    postgres:latest

$ docker exec --interactive --tty tombstone psql -U postgres
```

### Run
```
$ docker run \
    --detach \
    --network kate
    --publish 8000:5000 \
    --mount type=volume,src=daisy,target=/etc/daisy
    --env POSTGRES_HOST=tombstone
    --env POSTGRES_USER=postgres
    --env POSTGRES_PASSWORD=aneducatedman
    --env POSTGRES_DATABASE=postgres
    --name huckleberry \
    dockholliday
```

### Shell
```
$ docker exec --interactive --tty huckleberry sh
```

### System
Development:
```
$ docker compose -f docker-compose.dev.yml up -d
```
Production:
```
$ docker compose up -d
```

### Flask
```
$ venv/bin/pyuwsgi --http 0.0.0.0:8000 --master --module wsgi:app
```

### Stats
```
$ uwsgi --connect-and-read 127.0.0.1:8001
```
