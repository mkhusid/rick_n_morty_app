from pydantic import BaseModel, HttpUrl
from typing import List


class Episode(BaseModel):
    id: int
    name: str
    air_date: str
    episode: str
    characters: List[HttpUrl]
    url: HttpUrl
    created: str
