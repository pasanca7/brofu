import asyncio
import datetime
from sqlalchemy.future import select
from sqlalchemy import text

from backend.models.Player import Player
from backend.models.Game import Level
from backend.utils.logger import logger
from backend.ETL.players import pipeline
from backend.utils.database import Base, engine, AsyncSessionLocal


async def populate_db(db) -> None:
    logger.info("=========== Populating Players ===========")
    pipeline(path_file="backend/inputs/transfermarkt_players.csv")
    await db.execute(text("ALTER SEQUENCE players_id_seq RESTART WITH 1391240"))
    await db.commit()
    logger.info("=========== Populating levels ===========")
    await load_levels(db)


async def load_levels(db):
    await load_sevilla_2007(db)
    await load_barca_2011(db)


async def load_sevilla_2007(db):
    player_ids = [
        15956,
        7563,
        37906,
        58341,
        3573,
        646743,
        45314,
        34495,
        262365,
        15951,
        1443,
        15955,
        58789,
        16651,
        7782,
        39783,
        27471,
        15381,
    ]

    missing_players = [
        Player(
            first_name="Ivica",
            last_name="Dragutinovic",
            name="Ivica Dragutinovic",
            nationality="RS",
            date_of_birth=datetime.datetime(1975, 11, 13),
            position="DF",
            sub_position="CB",
        ),
        Player(
            first_name="Aitor",
            last_name="Ocio",
            name="Aitor Ocio",
            nationality="ES",
            date_of_birth=datetime.datetime(1976, 11, 28),
            position="DF",
            sub_position="CB",
        ),
        Player(
            first_name="David",
            last_name="Castedo",
            name="David Castedo",
            nationality="ES",
            date_of_birth=datetime.datetime(1974, 1, 26),
            position="DF",
            sub_position="LB",
        ),
        Player(
            first_name="Andreas",
            last_name="Hinkel",
            name="Andreas Hinkel",
            nationality="DK",
            date_of_birth=datetime.datetime(1982, 3, 26),
            position="DF",
            sub_position="LB",
        ),
        Player(
            first_name="Renato",
            last_name="Dirnei",
            name="Renato Dirnei",
            nationality="BR",
            date_of_birth=datetime.datetime(1976, 11, 28),
            position="MD",
            sub_position="MD",
        ),
        Player(
            first_name="Jesuli",
            last_name="Mora",
            name="Jesuli",
            nationality="ES",
            date_of_birth=datetime.datetime(1976, 11, 28),
            position="MD",
            sub_position="CF",
        ),
        Player(
            first_name="Fernando",
            last_name="Sales",
            name="Fernando Sales",
            nationality="ES",
            date_of_birth=datetime.datetime(1977, 9, 12),
            position="FW",
            sub_position="RW",
        ),
        Player(
            first_name="Kepa",
            last_name="Blanco",
            name="Kepa Blanco",
            nationality="ES",
            date_of_birth=datetime.datetime(1976, 11, 28),
            position="FW",
            sub_position="ST",
        ),
        Player(
            first_name="Ernesto Javier",
            last_name="Chevantón",
            name="Chevantón",
            nationality="UY",
            date_of_birth=datetime.datetime(1980, 8, 12),
            position="FW",
            sub_position="ST",
        ),
        Player(
            first_name="Luis",
            last_name="Fabiano",
            name="Luis Fabiano",
            nationality="BR",
            date_of_birth=datetime.datetime(1980, 11, 8),
            position="FW",
            sub_position="ST",
        ),
        Player(
            first_name="Frédéric",
            last_name="Kanouté",
            name="Frédéric Kanouté",
            nationality="ML",
            date_of_birth=datetime.datetime(1977, 9, 2),
            position="FW",
            sub_position="ST",
        ),
    ]

    result = await db.execute(select(Player).where(Player.id.in_(player_ids)))
    sevilla_players = result.scalars().all()

    db.add_all(missing_players)

    all_players = sevilla_players + missing_players

    level = Level(
        team="Sevilla F.C.",
        season="2005-2006",
        logo_url="https://img.uefa.com/imgml/TP/teams/logos/100x100/52714.png",
        players=all_players,
    )

    db.add(level)
    await db.commit()
    await db.refresh(level)
    logger.info("Sevilla F.C. 2006-2007 level added successfully")


async def load_barca_2011(db):
    level = Level(
        team="F.C. Barcelona",
        season="2010-2011",
        logo_url="https://img.uefa.com/imgml/TP/teams/logos/100x100/50080.png",
    )

    db.add(level)
    await db.commit()
    await db.refresh(level)
    logger.info("F.C. Barcelona 2010-2011 level added successfully")


async def init_db() -> None:
    async with AsyncSessionLocal() as session:
        for table in reversed(Base.metadata.sorted_tables):
            await session.execute(
                text(f"TRUNCATE {table.name} RESTART IDENTITY CASCADE;")
            )
        await session.commit()
        logger.info("Tables truncated successfully")

        await populate_db(session)
        logger.info("Data populated successfully")


if __name__ == "__main__":
    asyncio.run(init_db())
