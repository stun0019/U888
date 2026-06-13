from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import soccer, nba, mlb

app = FastAPI(
    title="Sports AI Platform API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(soccer.router, prefix="/soccer")
app.include_router(nba.router, prefix="/nba")
app.include_router(mlb.router, prefix="/mlb")


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "sports-ai-platform"
    }
