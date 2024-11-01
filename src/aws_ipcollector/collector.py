import requests




class AwsIpCollector:
    def __init__(self, url: str) -> None:
        self.url = url
        self.headers = {
            "Accept": "application/json"
        }
    
    def get_ranges(self) -> dict:
        response = requests.get(url=self.url, headers=self.headers)
        return response.json()