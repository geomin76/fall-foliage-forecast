from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID, uuid4

class DataEntry(BaseModel):
    blob_url: str
    timestamp: datetime
    color_percentage: float
    location_id: str
    id: UUID = Field(default_factory=uuid4)