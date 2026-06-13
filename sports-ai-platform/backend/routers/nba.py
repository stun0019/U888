from fastapi import APIRouter
from services.basketball_api import fetch_nba_matches

router = APIRouter()

@router.get("/matches")
async def matches():
    return await fetch_nba_matches()
