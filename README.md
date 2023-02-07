## Dockholliday

This is a simple containerized Flask application.

### Build
```
$ docker build --tag dockholliday .
```

### Run
```
$ docker run --detach --publish 8000:5000 --name huckleberry dockholliday
```
