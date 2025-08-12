import io
import pandas as pd
import psycopg2

from backend.utils.logger import logger
from backend.settings import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD


def load(df: pd.DataFrame):
    logger.info("Loading data using COPY...")

    # Exporta el DataFrame a CSV en memoria
    buffer = io.StringIO()
    df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)

    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host="localhost",
        port=5432,
    )
    cur = conn.cursor()

    try:
        cur.copy_expert(sql="COPY players FROM STDIN WITH CSV", file=buffer)
        conn.commit()
        logger.info("Data successfully loaded.")
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
