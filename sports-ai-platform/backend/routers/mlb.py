from fastapi import APIRouter
from services.mlb_api import get_mlb_matches

router = APIRouter()

@router.get("/matches")
async def matches():
    return await get_mlb_matches()
