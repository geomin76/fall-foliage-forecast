from pydantic import BaseModel
from datetime import datetime

class DataEntry(BaseModel):
    blob_url: str
    timestamp: datetime
    color_percentage: float
    location_id: str