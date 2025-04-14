# Rick and Morty File Downloader

This project contains client module to handle requests to the Rick and Morty API,
and a FastAPI application to expose endpoints for downloading characters, episodes, and locations data.


## Prerequisites
- Python 3.9+
- Pip or another Python package manager

## Setup and Run

1. Create and activate a virtual environment:
```bash
cd /Users/mkhusid/Desktop/Code/python/rick_n_morty_app
python -m venv venv
source venv/bin/activate
```


2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the FastAPI app using Uvicorn:
```bash
uvicorn app.main:app
```

4. Opend Swagger docs by this URL:

[http://localhost:8000/docs](#)
