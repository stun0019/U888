from fastapi import APIRouter
from services.basketball_api import get_nba_matches

router = APIRouter()

@router.get("/matches")
async def matches():
    return await get_nba_matches()
