from pydantic import BaseModel, HttpUrl
from typing import List


class Location(BaseModel):
    id: int
    name: str
    type: str
    dimension: str
    residents: List[HttpUrl]
    url: HttpUrl
    created: str
