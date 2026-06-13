from fastapi import APIRouter
from services.ai_engine import win_probability

router = APIRouter()

@router.get("/predict")
def predict(home: int = 50, away: int = 50):

    result = win_probability(home, away)

    return {
        "home_win_rate": result["home"],
        "away_win_rate": result["away"]
    }
