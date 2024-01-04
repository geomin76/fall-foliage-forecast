import requests
import os
from dotenv import load_dotenv
from service.model import SkyWatchData

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

def get_all_results_from_pipeline(pipeline_id: str):
    results = get_results_from_pipeline(pipeline_id)
    return results if results else None

def get_pipelines():
    response = requests.get("https://api.skywatch.co/earthcache/pipelines", headers=headers)
    results = response.json()['data']
    return [result['id'] for result in results]

def get_pipelines_data():
    response = requests.get("https://api.skywatch.co/earthcache/pipelines", headers=headers)
    results = response.json()['data']
    dictionary = {}
    for result in results:
        dictionary[result["id"]] = result
    return dictionary

def create_new_pipeline(data):
    response = requests.post("https://api.skywatch.co/earthcache/pipelines", headers=headers, json=data)
    return response.status_code

def delete_pipelines_call(data):
    response = requests.delete("https://api.skywatch.co/earthcache/pipelines", headers=headers, params=data)
    return response