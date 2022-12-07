import json
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ImageModel(BaseModel):
    object_id: int
    title: str
    site_name: str
    artist: str = None
    creation_date: str = None
    notes: str
    web_link: str
    image_url: str

class ResourceModel(BaseModel):
    resources: List[ImageModel]

@app.get('/api/images', response_model=ResourceModel) # this is a decorator
def list_items():
    return get_resources()

def get_resources():
    data = json.load(open('db.json')) # this could also call a db
    return ResourceModel.parse_obj(data)

@app.get('/api/images/{object_id}', response_model=ImageModel) # this is a decorator
def get_item(object_id:int):
    resource_model = get_resources()
    for image_model in resource_model.resources:
        if image_model.object_id == object_id:
            return image_model