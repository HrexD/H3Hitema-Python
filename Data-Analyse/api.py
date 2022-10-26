from fastapi import FastAPI

import uvicorn

from typing import Optional

from pydantic import BaseModel

app = FastAPI()


class CoordIn(BaseModel):
    password: str
    lat: float
    lon: float
    zoom: Optional[int] = None


class Coord0ut(BaseModel):

    lat: float
    lon: float
    zoom: Optional[int] = None
# get


@app.get("/")
async def hello_world():
    return {"hello": "world"}


@app.post("/position/", response_model=Coord0ut)
async def make_position(coord: CoordIn):
    return {"new_coord": coord.dict()}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
