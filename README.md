https://github.com/ArjanCodes/2022-docker




Run web server
```
    uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

List of all processes listening port

```
    lsof -n -i4TCP:8080

    PID is the second field. Then, kill that process:

    kill -9 PID
```


## Usage

As a first step, install Docker (see: https://www.docker.com) and install the requirements:

```
pip install -r requirements.txt
```

This is how you run the code locally (without Docker):

```
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

Build and run the Docker image locally, as follows:

```
docker build -t channel-api .
docker run -d -p 8080:80 channel-api
```

In order to run the example server with docker compose, use this:

```
docker-compose up --build
```

If you use docker compose and you make a minor change in the file, you can now see how everything is updated and the server is restarted automatically.