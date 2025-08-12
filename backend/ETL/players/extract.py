import pandas as pd

from backend.utils.logger import logger


def extract(path_file: str) -> pd.DataFrame:
    logger.info(f"Extracting data from {path_file}")
    try:
        df = pd.read_csv(
            filepath_or_buffer=path_file,
            usecols=[
                "player_id",
                "name",
                "first_name",
                "last_name",
                "position",
                "sub_position",
                "country_of_citizenship",
                "date_of_birth",
            ],
        )
    except FileNotFoundError as e:
        logger.error(f"Error: File not found in {path_file}. {e}")
        raise e
    logger.info(f"Data extracted successfully.")
    return df
