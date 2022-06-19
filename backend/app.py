from lib.bucket import bucket_goes_here
from lib.types import APIGWLambdaEvent
from aws_lambda_powertools.utilities.typing import LambdaContext

def handler(event: APIGWLambdaEvent, context: LambdaContext):
    print("Hello world")
    bucket_goes_here()
    return [
        { 
            'event_name' : "Makers hackathon",
            'event_location': "Makers Academy",
            'event_date': "July 20th"
        },
        { 
            'event_name' : "Makers anniversary",
            'event_location': "Makers Academy",
            'event_date': "August 28th"
        },
          { 
            'event_name' : "Makers yoga",
            'event_location': "Makers Academy",
            'event_date': "October 15th"
        },
            { 
            'event_name' : "Makers interview practice",
            'event_location': "Makers Academy",
            'event_date': "December 31st"
        },
              { 
            'event_name' : "Makers charity ball",
            'event_location': "Makers Academy",
            'event_date': "February 11th"
        }
    ]
    

