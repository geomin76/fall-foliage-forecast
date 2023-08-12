import requests
import os
from dotenv import load_dotenv
from model import SkyWatchData

load_dotenv()

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-api-key': os.environ['EARTHCACHE_KEY']
}

def get_results_from_pipeline(pipeline_id: str):
    response = requests.get("https://api.skywatch.co/earthcache/pipelines/{}/interval_results?sort=asc".format(pipeline_id), headers=headers)
    results = response.json()['data']
    returned_data = []
    for result in results:
        if result:
            for inner_result in result['results']:
                obj: SkyWatchData = SkyWatchData(visual_url=inner_result['visual_url'], capture_time=inner_result['capture_time'])
                returned_data.append(obj)
    return returned_data

def get_most_recent_result_from_pipeline(pipeline_id: str):
    results = get_results_from_pipeline(pipeline_id)
    return results[-1] if results else None

def get_pipelines():
    response = requests.get("https://api.skywatch.co/earthcache/pipelines", headers=headers)
    results = response.json()['data']
    return [result['id'] for result in results]