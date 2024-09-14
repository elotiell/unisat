import requests
from .config import PROXY

def check_proxy():
    try:
        response = requests.get("http://api.ipify.org?format=json", proxies=PROXY)
        print(f"Current IP: {response.json()['ip']}")
    except Exception as e:
        print(f"Proxy error: {e}")

def get_proxies():
    return PROXY 
