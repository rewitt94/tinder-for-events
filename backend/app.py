from lib.bucket import bucket_goes_here
from lib.types import APIGWLamdaEvent

def main(event: APIGWLamdaEvent):
    print("Hello world")
    bucket_goes_here()

main()