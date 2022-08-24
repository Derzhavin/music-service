from fastapi import Depends
from app.repositories.MusicTrackRepository import MusicTrackRepository


class MusicTrackService:

    def __init__(self, music_track_repository: MusicTrackRepository = Depends()):
        self.__music_track_repository = music_track_repository

    def get_music_tracks(self, skip: int = 0, limit: int = 5):
        music_tracks, total = self.__music_track_repository.get(skip, limit)
        return music_tracks, total
