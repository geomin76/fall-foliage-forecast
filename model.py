from pydantic import BaseModel, Field
from datetime import datetime

class DataEntry(BaseModel):
    blob_url: str
    timestamp: datetime
    color_percentage: float
    location_id: str

class SkyWatchData(BaseModel):
    visual_url: str
    capture_time: str