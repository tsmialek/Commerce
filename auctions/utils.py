import requests
from .models import *


def is_valid_image_url(url):
    if url is None:
        return True
    try:
        response = requests.head(url)
        return response.status_code == 200 and response.headers.get('Content-Type', '').startswith('image/')
    except requests.RequestException:
        return False