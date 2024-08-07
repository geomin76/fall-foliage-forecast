import json
from service.skywatch_call import create_new_pipeline, delete_pipelines_call

# create pipelines based on old data and increment the year
def create_pipeline(logger, json_file):
    dictionary = None
    with open(json_file) as f:
        dictionary = json.load(f)
        
    for pipeline_id in dictionary:
        pipeline_data = dictionary[pipeline_id]
        logger.info("Creating pipeline for {}".format(pipeline_data["name"]))

        start_date = pipeline_data["start_date"]
        arr = start_date.split("-")
        arr[0] = str(int(arr[0]) + 1)
        start_date = "-".join(arr)

        end_date = pipeline_data["end_date"]
        arr = end_date.split("-")
        arr[0] = str(int(arr[0]) + 1)
        end_date = "-".join(arr)

        # forming data
        post_data = {
            "name": pipeline_data["name"],
            "start_date": start_date,
            "end_date": end_date,
            "aoi": pipeline_data["aoi"],
            "min_aoi_coverage_percentage": pipeline_data["min_aoi_coverage_percentage"],
            "interval": pipeline_data["interval"],
            "output": pipeline_data["output"],
            "result_delivery": pipeline_data["result_delivery"],
            "max_cost": 0
        }

        create_new_pipeline(post_data)

        logger.info("Created pipeline for {} with start_date {}".format(pipeline_data["name"], start_date))



# delete the pipelines
def delete_pipelines(logger, json_file):
    dictionary = None
    with open(json_file) as f:
        dictionary = json.load(f)

    query_param = []
    for pipeline_id in dictionary:
        query_param.append(pipeline_id)
        logger.info("Deleting pipeline_id {}".format(pipeline_id))
    
    ids = ",".join(query_param)
    
    delete_pipelines_call({"ids": ids})
    
