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



## Deploying to AWS
- Create an AWS account
- Install Docker
- Install AWS CLI (https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Configure AWS CLI (https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
- Create an Elastic Container Registry > Repository
- Build Docker container (see above)
- Docker login to AWS Elastic Container Registry (https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)
- Tag container with AWS required naming
```
    docker tag tinder-for-events 063667696408.dkr.ecr.eu-west-2.amazonaws.com/tinder-for-events:lambda
```
- Push container to AWS Elastic Container Registry
```
    docker push 063667696408.dkr.ecr.eu-west-2.amazonaws.com/tinder-for-events:lambda
```
- Create Lambda function using Docker image (choose arm64 if container was built on mac M1)
- Create API Gateway > HTTP Api with integration to respective Lambda function 