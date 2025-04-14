''' Characters Controller.
This module contains the CharactersController class which handles
the logic for interacting with character-related endpoints.

In later versions more logic will be added here to handle specific character-related tasks.
'''
from typing import Dict
from app import utils
from app.models.character import Character
from client.rm_client import RickAndMortyClient


class CharactersController:
    ''' This class is responsible for handling character-related logic.'''

    def __init__(self, rm_client: RickAndMortyClient):
        self.rm_client = rm_client

    async def download_all_data(self) -> Dict[str, str]:
        """
        Download all characters data from the Rick and Morty API
        and parse it into a list of Character objects.
        """
        filename = "characters_data.json"
        async with self.rm_client() as client:
            characters = await client.get_characters()
            parsed_data = [Character(**character) for character in characters]
            file_path = await utils.save_json_to_file(parsed_data, filename)
            return { 'fname': filename, 'path': file_path }
