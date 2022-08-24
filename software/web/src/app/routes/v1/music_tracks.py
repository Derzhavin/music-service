from fastapi import Depends, APIRouter
from fastapi_pagination import Page, Params

from app.models.view.music_track import MusicTrackOut
from app.services.MusicTrackService import MusicTrackService

MusicTracksRouter = APIRouter(prefix='/v1')


@MusicTracksRouter.get("/compositions", tags=['compositions'], response_model=Page[MusicTrackOut])
async def music_tracks(page: int = 1, size: int = 5,
                       music_track_service: MusicTrackService = Depends()):
    skip = (page - 1) * size
    limit = size
    compositions, total = music_track_service.get_music_tracks(skip, limit)

    params = Params()
    params.page = page
    params.size = size

    page = Page.create(compositions, total, params)
    return page
