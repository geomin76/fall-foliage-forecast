import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-api-key': os.environ['EARTHCACHE_KEY']
}

response = requests.get("https://api.skywatch.co/earthcache/pipelines/f14b43e2-3568-11ee-ac6d-82bf3e71e06a/interval_results?sort=asc", headers=headers)
results = response.json()['data']
for result in results:
    print(result['results'])