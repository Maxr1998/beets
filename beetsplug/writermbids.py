from beets.plugins import BeetsPlugin
from beets.dbcore import types

MB_COMPOSERIDS = "mb_composerids"
MB_LYRICISTIDS = "mb_lyricistids"
MB_ARRANGERIDS = "mb_arrangerids"


class WriterMbidsPlugin(BeetsPlugin):
    item_types = {
        MB_COMPOSERIDS: types.MULTI_VALUE_DSV,
        MB_LYRICISTIDS: types.MULTI_VALUE_DSV,
        MB_ARRANGERIDS: types.MULTI_VALUE_DSV,
    }

    def __init__(self):
        super().__init__()
        self.register_listener("mb_track_extract", self.track_extract)

    @staticmethod
    def track_extract(data):
        recording = data
        composer_mbids = []
        lyricist_mbids = []
        arranger_mbids = []

        for work_relation in recording.get("work-relation-list", ()):
            if work_relation["type"] != "performance":
                continue

            work = work_relation["work"]
            for artist_relation in work.get("artist-relation-list", ()):
                if "type" in artist_relation:
                    artist_type = artist_relation["type"]
                    if artist_type == "composer":
                        composer_mbids.append(artist_relation["artist"]["id"])
                    elif artist_type == "lyricist":
                        lyricist_mbids.append(artist_relation["artist"]["id"])

        for artist_relation in recording.get("artist-relation-list", ()):
            if "type" in artist_relation:
                artist_type = artist_relation["type"]
                if artist_type == "arranger":
                    arranger_mbids.append(artist_relation["artist"]["id"])

        info = {}
        if composer_mbids:
            info[MB_COMPOSERIDS] = composer_mbids
        if lyricist_mbids:
            info[MB_LYRICISTIDS] = lyricist_mbids
        if arranger_mbids:
            info[MB_ARRANGERIDS] = arranger_mbids
        return info
