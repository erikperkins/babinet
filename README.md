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

### Run
```
$ docker run \
    --detach \
    --publish 8000:5000 \
    --mount type=volume,src=daisy,target=/etc/daisy
    --name huckleberry \
    dockholliday
```

### Shell
```
$ docker exec --interactive --tty huckleberry sh
```
