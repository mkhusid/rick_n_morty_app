''' Characters Controller.
This module contains the CharactersController class which handles
the logic for interacting with character-related endpoints.

In later versions more logic will be added here to handle specific character-related tasks.
'''
from typing import Dict
from client.rm_client import RickAndMortyClient
from app.models.character import Character


class CharactersController:
    ''' This class is responsible for handling character-related logic.'''

    def __init__(self, rm_client: RickAndMortyClient):
        self.rm_client = rm_client

    async def download_all_data(self) -> Dict[str, list[Character]]:
        """
        Download all characters data from the Rick and Morty API
        and parse it into a list of Character objects.
        """
        filename = "characters_data.json"
        async with self.rm_client() as client:
            characters = await client.get_characters()
            parsed_data = [Character(**character) for character in characters]
            return {"characters": parsed_data, "fname": filename}
