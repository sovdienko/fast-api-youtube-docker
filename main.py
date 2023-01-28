""" Simple API server for Docker enrolment """
import json
from dataclasses import dataclass, field

from fastapi import FastAPI, HTTPException, Response

app = FastAPI()

@dataclass
class Channel:
    """ Youtube channals data structure """
    id: str
    name: str
    tags: list[str] = field(default_factory=list)
    description: str = ""

channels: dict[str, Channel] = {}

with open("channels.json",'r',encoding='utf-8') as file:
    channels_row = json.load(file)
    for channel_row in channels_row:
        channel = Channel(**channel_row)
        channels[channel.id] = channel


@app.get("/")
def read_root() -> Response:
    """ Check if server is runnung """
    return Response("The server is running...")


@app.get("/channels/{channel_id}", response_model=Channel)
def read_item(channel_id: str) -> Channel:
    """ Provides Youtube channels information """
    if channel_id not in channels:
        raise HTTPException(status_code=404, detail="Channel not found")
    return channels[channel_id]
