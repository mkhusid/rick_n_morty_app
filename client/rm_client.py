''' Rick and Morty API Client'''
from enum import Enum
import aiohttp

# Define the base URL for the Rick and Morty API (should be moved to env or config file)
BASE_URL = "https://rickandmortyapi.com/api"


class ResourceType(Enum):
    ''' Enum for resource types in the Rick and Morty API '''
    CHARACTER = "character"
    LOCATION = "location"
    EPISODE = "episode"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class RickAndMortyClient:
    ''' Aync client for the Rick and Morty API
    Implemented  as async context manager
    Sample Usage:
        async with RickAndMortyClient() as client:
            characters = await client.get_characters()
            locations = await client.get_locations()
            episodes = await client.get_episodes()
    '''
    base_url = BASE_URL

    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *exc_details):
        await self.session.close()

    async def _fetch_all_data(self, resource_enpoint: ResourceType):
        ''' Fetch complete data for a given resource endpoint
        Args:
            resource_enpoint (str): The endpoint to fetch data from
        Returns:
            list: A list of all items from the endpoint
        '''
        url = f"{self.base_url}/{resource_enpoint}"
        results = []

        while url:
            async with self.session.get(url) as response:
                data = await response.json()
                results.extend(data.get("results", []))
                metadata = data.get("info", None)
                if metadata:
                    next_page = metadata.get("next", None)
                    url = next_page
                else:
                    break

        return results

    async def get_characters(self):
        ''' Fetch all characters from the API '''
        try:
            return await self._fetch_all_data(ResourceType.CHARACTER)
        except aiohttp.ClientError as e:
            print(f"Failed to fetch characters: {e}")
            return []

    async def get_locations(self):
        ''' Fetch all locations from the API '''
        try:
            return await self._fetch_all_data(ResourceType.LOCATION)
        except aiohttp.ClientError as e:
            print(f"Failed to fetch locations: {e}")
            return []

    async def get_episodes(self):
        ''' Fetch all episodes from the API '''
        try:
            return await self._fetch_all_data(ResourceType.EPISODE)
        except aiohttp.ClientError as e:
            print(f"Failed to fetch episodes: {e}")
            return []
