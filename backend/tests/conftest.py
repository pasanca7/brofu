import pytest
import pytest_asyncio
import datetime
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import StaticPool

from backend.main import app
from backend.utils.database import Base, get_db
from backend.utils.auth import hash_password
from backend.models.Player import Player
from backend.models.User import User

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    echo=True,
)

TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


def override_get_db():
    db = TestingSessionLocal()
    yield db
    db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest_asyncio.fixture(scope="function")
async def setup_db(client, test_user):
    async with engine.begin() as conn:
        global TOKEN_USER
        await conn.run_sync(Base.metadata.create_all)
        async with TestingSessionLocal() as session:
            user = test_user
            session.add(user)
            await session.commit()
        TOKEN_USER = client.post(
            "/login",
            data={
                "username": "pasanca_7",
                "password": "securepassword",
            },
        ).json()["access_token"]
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def db(setup_db):
    async with TestingSessionLocal() as session:
        yield session
        await session.rollback()


@pytest.fixture
def test_user():
    return User(
        username="pasanca_7",
        email="pasanca_7@example.com",
        first_name="Pablo",
        second_name="de los Santos Carrión",
        hashed_password=hash_password("securepassword"),
    )


@pytest.fixture
def player_1():
    return Player(
        id=15956,
        first_name="Jesús",
        last_name="Navas",
        name="Jesús Navas",
        date_of_birth=datetime.date(1985, 11, 21),
        position="DF",
        sub_position="RB",
        nationality="ESP",
    )


@pytest.fixture
def players(player_1):
    return [
        player_1,
        Player(
            id=79422,
            first_name="Keylor",
            last_name="Navas",
            name="Keylor Navas",
            position="GK",
            sub_position="GK",
            date_of_birth=datetime.date(1986, 12, 15),
        ),
    ]


@pytest_asyncio.fixture
async def db_with_player(db, players):
    await insert_test_player(db, players)
    return db


async def insert_test_player(session: AsyncSession, players: list[Player]):
    session.add_all(players)
    await session.commit()
