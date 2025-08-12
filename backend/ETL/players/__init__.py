from backend.ETL.players.extract import extract
from backend.ETL.players.transform import transform
from backend.ETL.players.load import load
from backend.utils.logger import logger


def pipeline(path_file: str) -> None:
    logger.info("Pipeline started")
    df = extract(path_file)
    df = transform(df)
    load(df)
