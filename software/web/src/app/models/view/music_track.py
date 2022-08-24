from pydantic import BaseModel


class MusicTrackOut(BaseModel):
    track_name: str

    class Config:
        orm_mode = True
