''' This module contains utility functions for the application. '''
import json
from pathlib import Path
from pydantic import BaseModel

async def save_json_to_file(data: list[BaseModel], filename: str) -> Path:
    ''' Save data to a JSON file'''
    file_path = Path(f"./data/{filename}")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as f:
        parsed_data = [item.model_dump(mode='json') for item in data]
        json.dump(parsed_data, f, ensure_ascii=False, indent=4)

    return file_path
