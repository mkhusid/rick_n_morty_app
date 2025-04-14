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
        parsed_data = await character_controller.download_all_data()
        file_path = await utils.save_json_to_file(parsed_data['characters'], parsed_data['fname'])
        return FileResponse(file_path, media_type='application/json', filename=parsed_data['fname'])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
