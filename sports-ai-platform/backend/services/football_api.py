import httpx

BASE_URL = "https://www.thesportsdb.com/api/v1/json/3"

async def fetch_soccer_matches():

    async with httpx.AsyncClient() as client:

        res = await client.get(
            f"{BASE_URL}/eventsnextleague.php?id=4328"
        )

        data = res.json()

        events = data.get("events", [])

        return [
            normalize_event(e, "soccer")
            for e in events
        ]


def normalize_event(e, sport):

    return {
        "sport": sport,
        "league": e.get("strLeague"),
        "home": e.get("strHomeTeam"),
        "away": e.get("strAwayTeam"),
        "home_score": None,
        "away_score": None,
        "time": build_time(e),
        "status": "upcoming"
    }


def build_time(e):

    date = e.get("dateEvent")
    time = e.get("strTime") or "00:00:00"

    return f"{date}T{time}Z"
