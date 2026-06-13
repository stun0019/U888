from fastapi import APIRouter
from services.football_api import get_next_matches

router = APIRouter()

@router.get("/matches")
async def matches():
    return await get_next_matches()
