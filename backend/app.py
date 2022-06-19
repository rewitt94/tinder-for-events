from lib.bucket import bucket_goes_here
from lib.types import APIGWLambdaEvent
from aws_lambda_powertools.utilities.typing import LambdaContext

def handler(event: APIGWLambdaEvent, context: LambdaContext):
    print("Hello world")
    bucket_goes_here()
