from pydantic import BaseModel


from pydantic import BaseModel, HttpUrl
from typing import List
from typing import Optional


class Origin(BaseModel):
    name: str
    url: Optional[str] = None


class Location(BaseModel):
    name: str
    url: Optional[str] = None


class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: Origin
    location: Location
    image: HttpUrl
    episode: List[HttpUrl]
    url: HttpUrl
    created: str
