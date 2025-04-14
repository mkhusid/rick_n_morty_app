''' Router for characters data '''
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.controllers.characters_controller import CharactersController
from client.rm_client import RickAndMortyClient
import app.utils as utils

router = APIRouter(prefix="/characters", tags=["Characters"])
character_controller = CharactersController(rm_client=RickAndMortyClient)


@router.get("/download", response_class=FileResponse)
async def download_characters_data():
    """
    Endpoint to download all characters data from the Rick and Morty API.
    """
    try:
        file = await character_controller.download_all_data()
        return FileResponse(file['path'], media_type='application/json', filename=file['fname'])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
