''' Router for episodes data '''
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.controllers.episodes_controller import EpisodesController
from client.rm_client import RickAndMortyClient
import app.utils as utils

router = APIRouter(prefix="/episodes", tags=["Episodes"])
episode_controller = EpisodesController(rm_client=RickAndMortyClient)


@router.get("/download", response_class=FileResponse)
async def download_characters_data():
    """
    Endpoint to download all episodes data from the Rick and Morty API.
    """
    try:
        file = await episode_controller.download_all_data()
        return FileResponse(file['path'], media_type='application/json', filename=file['fname'])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
