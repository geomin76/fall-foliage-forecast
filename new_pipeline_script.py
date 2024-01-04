from service.pipeline_data_tracker import dump_new_data
import logging
from service.recreate_pipelines import create_pipeline, delete_pipelines

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

year = "2024"
json_file = "./pipeline_data/{}_pipeline_data.json".format(year)

dump_new_data(year)
logger.info("Dumped previous year's pipeline data")

create_pipeline_status_code = create_pipeline(logger, json_file)
logger.info("Received a {} after create_pipeline call".format(str(create_pipeline_status_code)))

delete_pipeline_response = delete_pipelines(logger, json_file)
logger.info("Completed delete_pipeline call")