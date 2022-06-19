# tinder-for-events

# setup

- python3 -m venv .env (creates the env)
- source .env/bin/activate (activates the env)
- pip install -r ./requirements.txt
- install python vscode extension
- set python vscode interpreter to be $(which python)
- python -m pip install .

## Run locally 
docker build -t tinder-for-events .
docker run -p 9000:8080 tinder-for-events

## Local CURL requests 
```
curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"requestContext":{"http":{"method":"GET","path": "/helloworld"}}}'
```