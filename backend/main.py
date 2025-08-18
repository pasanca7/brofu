from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from backend.routers.players_router import router as players_router
from backend.routers.game_router import router as game_router
from backend.settings import ORIGINS

app = FastAPI(
    title="Brofu, do you remember the old days?",
    description="API for playing with lengendary football squads.",
    version="1.0.0",
)

api_router = APIRouter(prefix="/api")

app.include_router(players_router)
app.include_router(game_router)

# TODO: check allow methods and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Ready for the challenge?"}
