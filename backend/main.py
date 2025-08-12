from fastapi import FastAPI, APIRouter

from backend.routers.players_router import router as players_router
from backend.routers.game_router import router as game_router

app = FastAPI(
    title="Brofu, do you remember the old days?",
    description="API for playing with lengendary football squads.",
    version="1.0.0",
)

api_router = APIRouter(prefix="/api")

app.include_router(players_router)
app.include_router(game_router)


@app.get("/")
async def root():
    return {"message": "Ready for the challenge?"}
