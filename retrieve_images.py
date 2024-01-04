import requests 
from PIL import Image 
from service.dynamodb import get_data
from service.skywatch_call import get_pipelines, get_all_results_from_pipeline
import logging
from service.model import SkyWatchData

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

pipeline_ids = get_pipelines()
for pipeline_id in pipeline_ids:
    logger.info("Running fall foliage check for pipeline " + pipeline_id)
    # get most recent data from SkyWatch for a pipeline
    results: SkyWatchData = get_all_results_from_pipeline(pipeline_id)
    if not results:
        continue
    else:
        dynamodb_data = get_data(pipeline_id, enable_data=True)
        for result in results:
            url = result.visual_url

            # Get the photos
            file_name = url.split("/")[-1]
            data = requests.get(url).content 
            f = open("photos/" + file_name,'wb') 
            # Storing the image data inside the data variable to the file 
            f.write(data) 
            f.close() 