import httpx

# MLB Stats API（簡化版 mock endpoint）
API_BASE = "https://statsapi.mlb.com/api/v1"

async def get_mlb_matches():

    async with httpx.AsyncClient() as client:

        res = await client.get(
            f"{API_BASE}/schedule?sportId=1"
        )

        data = res.json()

        games = []

        for date in data.get("dates", []):

            for game in date.get("games", []):

                games.append({
                    "sport": "mlb",
                    "league": "MLB",
                    "home": game["teams"]["home"]["team"]["name"],
                    "away": game["teams"]["away"]["team"]["name"],
                    "time": game.get("gameDate"),
                    "status": game.get("status", {}).get("detailedState")
                })

        return games
