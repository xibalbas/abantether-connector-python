from typing import Dict
import requests


class AbantetherAPI:
    DEFAULT_TIMEOUT = 10
    BASE_URL = 'https://abantether.com/api/v1/'
    HOST = 'abantether.com'
    VERSION = 'v1'

    def __init__(self, api_key: str, timeout: int = None):
        self.api_key = api_key
        self.timeout = timeout or self.DEFAULT_TIMEOUT
        self.headers = {
            'Accept': 'application/json',
        }

    def _request(self, method: str, params: Dict = {}):
        pass


