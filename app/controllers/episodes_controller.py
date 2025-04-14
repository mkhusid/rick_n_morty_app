''' 
Episode Controller
This module contains the EpisodesController class which handles
the logic for interacting with episode-related endpoints.

In later versions more logic will be added here to handle specific episode-related tasks.
'''
from typing import Dict
from client.rm_client import RickAndMortyClient
from app.models.episode import Episode


class EpisodesController:
    ''' This class is responsible for handling character-related logic.'''

    def __init__(self, rm_client: RickAndMortyClient):
        self.rm_client = rm_client

    async def download_all_data(self) -> Dict[str, list[Episode]]:
        """
        Download all episodes data from the Rick and Morty API
        and parse it into a list of Episode objects.
        """
        filename = "episodes_data.json"
        async with self.rm_client() as client:
            episodes = await client.get_episodes()
            parsed_data = [Episode(**episode) for episode in episodes]
            return {"episodes": parsed_data, "fname": filename}
