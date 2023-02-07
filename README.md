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