''' Router for locations data '''
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.controllers.locations_controller import LocationsController
from client.rm_client import RickAndMortyClient
import app.utils as utils


router = APIRouter(prefix="/locations", tags=["Locations"])
location_controller = LocationsController(rm_client=RickAndMortyClient)

@router.get("/download", response_class=FileResponse)
async def download_locations_data():
    """
    Endpoint to download all locations data from the Rick and Morty API.
    """
    try:
        file = await location_controller.download_all_data()
        return FileResponse(file['path'], media_type='application/json', filename=file['fname'])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
