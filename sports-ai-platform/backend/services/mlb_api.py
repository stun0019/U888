import httpx

BASE_URL = "https://statsapi.mlb.com/api/v1"

async def fetch_mlb_matches():

    async with httpx.AsyncClient() as client:

        res = await client.get(
            f"{BASE_URL}/schedule?sportId=1"
        )

        data = res.json()

        matches = []

        for date_block in data.get("dates", []):

            for game in date_block.get("games", []):

                matches.append({
                    "sport": "mlb",
                    "league": "MLB",
                    "home": game["teams"]["home"]["team"]["name"],
                    "away": game["teams"]["away"]["team"]["name"],
                    "home_score": game["teams"]["home"].get("score"),
                    "away_score": game["teams"]["away"].get("score"),
                    "time": game.get("gameDate"),
                    "status": normalize_status(game)
                })

        return matches


def normalize_status(game):

    state = game.get("status", {}).get("detailedState", "")

    if state in ["Final", "Game Over"]:
        return "finished"

    return "upcoming"
