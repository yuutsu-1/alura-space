from enum import Enum

class AuthType(Enum):
    NO_AUTH = None,
    BASIC = 'BASIC'        ,
    BEARER_TOKEN = 'BEARER',
    API_KEY = 'API KEY'    ,
    OAUTH = 'OAUTH'