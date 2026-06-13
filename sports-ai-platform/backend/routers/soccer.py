from fastapi import APIRouter
from services.football_api import fetch_soccer_matches

router = APIRouter()

@router.get("/matches")
async def matches():
    return await fetch_soccer_matches()
