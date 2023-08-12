from color_analysis import color_analysis
from skywatch_call import get_pipelines, get_most_recent_result_from_pipeline
import requests
from model import SkyWatchData, DataEntry
import os
from dynamodb import insert_data

def main():
    # cron job to pull data from SkyWatch
    pipeline_ids = get_pipelines()
    for pipeline_id in pipeline_ids:
        result: SkyWatchData = get_most_recent_result_from_pipeline(pipeline_id)
        if not result:
            continue

        # TODO: if timestamp already exists for this location_id in dynamo, do not add

        img_data = requests.get(result.visual_url).content
        with open('temp.png', 'wb') as handler:
            handler.write(img_data)

        # run color_analysis on image
        percentage = color_analysis("./temp.png")

        try: os.remove("./temp.png")
        except OSError: pass

        # store data in dynamodb
        insert_data(DataEntry(
            blob_url = result.visual_url, 
            timestamp = result.capture_time,
            color_percentage = percentage,
            location_id = pipeline_id
        ))

if __name__ == "__main__":
    main()