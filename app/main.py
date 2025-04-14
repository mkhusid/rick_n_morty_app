''' Main entry point for the FastAPI application. '''
from fastapi import FastAPI
from app.routers import characters_router
from app.routers import episodes_router
from app.routers import locations_router

app = FastAPI()

app.include_router(characters_router.router, prefix="/api/v1")
app.include_router(episodes_router.router, prefix="/api/v1")
app.include_router(locations_router.router, prefix="/api/v1")

@app.get("/", tags=["Basics"])
async def root():
    """
    Root endpoint
    """
    return {"message": "Welcome to the Rick and Morty File Downloader API!"}


@app.get("/health", tags=["Basics"])
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "ok", "message": "This is Rick and Morty File Downloader API, have fun!"}
