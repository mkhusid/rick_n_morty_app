'''
Location Controller
This module contains the LocationController class which handles
the logic for interacting with location-related endpoints.

In later versions more logic will be added here to handle specific location-related tasks.
'''
from client.rm_client import RickAndMortyClient
from app.models.location import Location
from typing import Dict

class LocationsController:
    ''' This class is responsible for handling location-related logic.'''

    def __init__(self, rm_client: RickAndMortyClient):
        self.rm_client = rm_client

    async def download_all_data(self) -> Dict[str, list[Location]]:
        """
        Download all locations data from the Rick and Morty API
        and parse it into a list of Location objects.
        """
        filename = "locations_data.json"
        async with self.rm_client() as client:
            locations = await client.get_locations()
            parsed_data = [Location(**location) for location in locations]
            return {"locations": parsed_data, "fname": filename}
