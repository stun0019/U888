import httpx

API_BASE = "https://www.thesportsdb.com/api/v1/json/3"

async def get_nba_matches():

    async with httpx.AsyncClient() as client:

        res = await client.get(
            f"{API_BASE}/eventsnextleague.php?id=4387"
        )

        data = res.json()

        return [
            {
                "sport": "nba",
                "league": e.get("strLeague"),
                "home": e.get("strHomeTeam"),
                "away": e.get("strAwayTeam"),
                "time": f"{e.get('dateEvent')} {e.get('strTime')}",
                "status": "upcoming"
            }
            for e in data.get("events", [])
        ]
