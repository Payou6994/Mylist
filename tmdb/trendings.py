from .tmdb import Tmdb


class Trendings(Tmdb):
    _urls = {
        "all_day": "/trending/all/day",
        "all_week": "/trending/all/week",
        "movie_day": "/trending/movie/day",
        "movie_week": "/trending/movie/week",
        "tv_day": "/trending/tv/day",
        "tv_week": "/trending/tv/week",
        "person_day": "/trending/person/day",
        "person_week": "/trending/person/week"
    }

    def all_day(self):
        """
        Get all daily trending
        :param page: int
        :return:
        """
        return self._call(self._urls["all_day"], "")

    def all_week(self):
        """
        Get all weekly trending
        :param page: int
        :return:
        """
        return self._call(self._urls["all_week"], "")

    def movie_day(self, page=1):
        """
        Get movie daily trending
        :param page: int
        :return:
        """
        return self._call(self._urls["movie_day"], "page={}".format(page))

    def movie_week(self, page=1):
        """
        Get movie weekly trending
        :param page: int
        :return:
        """
        return self._call(self._urls["movie_week"], "page={}".format(page))

    def tv_day(self, page=1):
        """
        Get tv daily trending
        :param page: int
        :return:
        """
        return self._call(self._urls["tv_day"], "page={}".format(page))

    def tv_week(self, page=1):
        """
        Get tv weekly trending
        :param page: int
        :return:
        """
        return self._call(self._urls["tv_week"], "page={}".format(page))
