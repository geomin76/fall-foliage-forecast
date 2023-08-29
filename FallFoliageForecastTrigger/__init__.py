import datetime
import logging
from service.color_analysis import color_analysis
from service.skywatch_call import get_pipelines, get_most_recent_result_from_pipeline
import requests
from service.model import SkyWatchData, DataEntry
import os
from service.dynamodb import insert_data, get_data
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info('Python timer trigger function ran at %s UTC', utc_timestamp)
    
    # cron job to pull data from SkyWatch
    pipeline_ids = get_pipelines()
    for pipeline_id in pipeline_ids:
        logging.info("Running fall foliage check for pipeline " + pipeline_id)
        # get most recent data from SkyWatch for a pipeline
        result: SkyWatchData = get_most_recent_result_from_pipeline(pipeline_id)
        if not result:
            continue

        # if timestamp for a certain pipeline_id already exists, no need for duplicates and ignore
        dynamodb_data = get_data(pipeline_id)
        if len(dynamodb_data) > 0 and dynamodb_data[-1].timestamp == result.capture_time:
            logging.info("Data for pipeline {} already exists for timestamp: {}".format(pipeline_id, result.capture_time))
            continue

        # retrieving image from s3 and saving locally
        img_data = requests.get(result.visual_url).content
        with open('temp.png', 'wb') as handler:
            handler.write(img_data)

        # run color_analysis on image
        percentage = color_analysis("./temp.png")

        # remove image, and if image doesn't exist, pass
        try: os.remove("./temp.png")
        except OSError: pass

        # store data in dynamodb
        insert_data(DataEntry(
            blob_url = result.visual_url, 
            timestamp = result.capture_time,
            color_percentage = percentage,
            location_id = pipeline_id
        ))
        logging.info("Inserted data for pipeline " + pipeline_id + " and timestamp " + result.capture_time)

