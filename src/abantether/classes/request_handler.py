import requests

__all__ = ["RequestHandler"]


class RequestHandler:
    DEFAULT_TIMEOUT = 10

    def __init__(self, base_url: str, api_key: str, timeout: int = None):
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = timeout or self.DEFAULT_TIMEOUT
        self.headers = {
            'Authorization': f'Token {api_key}',
            'Accept': 'application/json'
        }

    def get(self, url, **kwargs):
        return self.session.get(self.base_url + url, timeout=self.timeout,
                                headers=self.headers, **kwargs)

    def post(self, url, **kwargs):
        return self.session.post(self.base_url + url, timeout=self.timeout,
                                 headers=self.headers, **kwargs)

    def put(self, url, **kwargs):
        return self.session.put(self.base_url + url, timeout=self.timeout,
                                headers=self.headers, **kwargs)

    def patch(self, url, **kwargs):
        return self.session.patch(self.base_url + url, timeout=self.timeout,
                                  headers=self.headers, **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(self.base_url + url, timeout=self.timeout,
                                   headers=self.headers, **kwargs)
