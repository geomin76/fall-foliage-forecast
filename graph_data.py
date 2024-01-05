from service.dynamodb import get_data
from service.skywatch_call import get_pipelines
import pandas as pd
import matplotlib.pyplot as plt
from service.pipeline_data_tracker import get_json_data
from service.model import DataEntry

year = "2023"
DF = pd.DataFrame()
json_data = get_json_data(year)
for pipeline_id in json_data:
    name = json_data[pipeline_id]["name"]
    datetimes = []
    values = []
    dynamodb_data = get_data(pipeline_id)
    for data in dynamodb_data:
        data: DataEntry = data
        datetimes.append(pd.to_datetime(data.timestamp))
        values.append(data.color_percentage)
    
    plt.plot(datetimes, values, label=name)

plt.legend()
plt.show()
        
    

