import requests
import requests.auth
from .enums import AuthType
from typing import Optional

class APIClient:
    def __init__(self, baseUrl: str                 ,
                 authType: Optional[AuthType] = None,
                 apiKey: Optional[str] = None       ,
                 username: Optional[str] = None     ,
                 password: Optional[str] = None):
        
        if authType and authType not in AuthType:
            raise ValueError(f"Invalid authType: {authType}")
        
        self.baseUrl = baseUrl
        self.authType = authType
        self.apiKey = apiKey  
        self.username = username
        self.password = password
        

    def build_headers(self, **kwargs) -> dict:
        headers = {}

        if self.authType == AuthType.API_KEY:
            if not self.apiKey:
                raise ValueError("API key must be provided for apiKey auth type.")
            
            headers['api_key'] = self.apiKey

        elif self.authType == AuthType.BEARER_TOKEN:
            if not self.apiKey:
                raise ValueError("Bearer token must be provided for BEARER_TOKEN auth type.")
            
            headers['Authorization'] = f"Bearer {self.apiKey}"
            
        elif self.authType == AuthType.BASIC:
            if not self.apiKey:
                raise ValueError("Basic auth must be provided username and password.")
            
            user, pwd = self.username, self.password
            
            headers['Authorization'] = f"Basic {requests.auth._basic_auth_str(user, pwd)}"
        
        if kwargs:
            for key, value in kwargs.items:
                headers[key] = value
                
        return headers
    
    def send_request(self, endpoint: str, 
                     method: str = "GET",
                     params: Optional[dict] = None,
                     json_data: Optional[dict] = None):
        
        url = f"{self.baseUrl}/{endpoint}"
        headers = self.build_headers(json_data) if json_data else None

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json_data,
                timeout=10
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None