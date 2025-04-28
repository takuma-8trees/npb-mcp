import requests

class OkaHiromiTracker:
    """
    SPAIA NPB APIを利用して、岡大海選手の成績情報を取得するクラス。
    """

    BASE_URL = "https://spaia.jp/baseball/npb/api"
    OKA_HIROMI_PERSON_ID = 1300044  # 修正
    OKA_HIROMI_PLAYER_ID = 1300044  # 修正

    def _get(self, endpoint: str, params: dict = None) -> dict:
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_profile(self) -> dict:
        """岡大海選手のプロフィール情報を取得"""
        return self._get("player_by_team", {"person_info_id": self.OKA_HIROMI_PERSON_ID})

    def get_career_hitting_stats(self) -> dict:
        """岡大海選手の通算（キャリア）打撃成績を取得"""
        return self._get("hitting_stats_career", {"playerId": self.OKA_HIROMI_PLAYER_ID})

    def get_season_hitting_stats(self, year: int) -> dict:
        """岡大海選手の指定年のシーズン打撃成績を取得"""
        return self._get("hitting_stats_by_year", {"player_id": self.OKA_HIROMI_PERSON_ID, "year": year})

    def get_monthly_hitting_stats(self, year: int) -> dict:
        """岡大海選手の指定年の月別打撃成績を取得"""
        return self._get("hitting_stats_by_month", {"player_id": self.OKA_HIROMI_PERSON_ID, "year": year})

    def get_game_by_game_hitting_stats(self, year: int) -> dict:
        """岡大海選手の指定年の試合別打撃成績を取得"""
        return self._get("hitting_stats_by_game", {"player_id": self.OKA_HIROMI_PERSON_ID, "year": year})

