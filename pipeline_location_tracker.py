from service.skywatch_call import get_pipelines_data
import json

with open("pipeline_data/2023_pipeline_data.json", "w") as outfile: 
    json.dump(get_pipelines_data(), outfile)