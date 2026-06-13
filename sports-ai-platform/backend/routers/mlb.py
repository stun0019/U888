from fastapi import APIRouter
from services.mlb_api import fetch_mlb_matches

router = APIRouter()

@router.get("/matches")
async def matches():
    return await fetch_mlb_matches()
