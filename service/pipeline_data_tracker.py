from service.skywatch_call import get_pipelines_data
import json

def dump_new_data(year):
    with open("pipeline_data/{}_pipeline_data.json".format(year), "w") as outfile: 
        json.dump(get_pipelines_data(), outfile)

def get_json_data(year):
    with open("pipeline_data/{}_pipeline_data.json".format(year), "r") as outfile: 
        d = json.loads(outfile.read())
        return d
