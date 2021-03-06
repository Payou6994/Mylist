import requests
import os
from .exceptions import TMDbException


class Tmdb(object):
    TMDB_API_KEY = "TMDB_API_KEY"
    TMDB_LANGUAGE = "TMDB_LANGUAGE"

    def __init__(self):
        self._base = "https://api.themoviedb.org/3"
        if os.environ.get(self.TMDB_LANGUAGE) is None:
            os.environ[self.TMDB_LANGUAGE] = "en-US"

    @property
    def api_key(self):
        return os.environ.get(self.TMDB_API_KEY)

    @api_key.setter
    def api_key(self, api_key):
        os.environ[self.TMDB_API_KEY] = str(api_key)

    @property
    def language(self):
        return os.environ.get(self.TMDB_LANGUAGE)

    @language.setter
    def language(self, language):
        os.environ[self.TMDB_LANGUAGE] = language

    def _call(self, action, append_to_response):
        if append_to_response:
            url = (
                f"{self._base}{action}?api_key={self.api_key}"
                f"&language={self.language}"
                f"&append_to_response={append_to_response}"
            )
        else:
            url = (
                f"{self._base}{action}?api_key={self.api_key}"
                f"&language={self.language}"
            )
        result = requests.get(url)

        rslt_json = result.json()

        if rslt_json["success"] is False:
            raise TMDbException(rslt_json["status_message"])

        return rslt_json
