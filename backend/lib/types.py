from typing import TypedDict

class HTTPRequestContext(TypedDict):
  method: str
  path: str
  
class RequestContext(TypedDict):
  time: str
  timeEpoch: str
  http: HTTPRequestContext
  
class APIGWLambdaEvent(TypedDict):
  body: str
  isBase64Encoded: bool
  headers: dict[str, str]
  requestContext: RequestContext