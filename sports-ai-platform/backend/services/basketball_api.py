import httpx

BASE_URL = "https://www.thesportsdb.com/api/v1/json/3"

async def fetch_nba_matches():

    async with httpx.AsyncClient() as client:

        res = await client.get(
            f"{BASE_URL}/eventsnextleague.php?id=4387"
        )

        data = res.json()

        return [
            {
                "sport": "nba",
                "league": e.get("strLeague"),
                "home": e.get("strHomeTeam"),
                "away": e.get("strAwayTeam"),
                "home_score": None,
                "away_score": None,
                "time": build_time(e),
                "status": "upcoming"
            }
            for e in data.get("events", [])
        ]


def build_time(e):
    return f"{e.get('dateEvent')}T{e.get('strTime') or '00:00:00'}Z"
