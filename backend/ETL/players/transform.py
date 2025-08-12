import pandas as pd
import pycountry

from backend.utils.logger import logger

MANUAL_CORRECTIONS = {
    "Cote d'Ivoire": "CI",
    "Korea, South": "KR",
    "Korea, North": "KP",
    "DR Congo": "CD",
    "Bosnia-Herzegovina": "BA",
    "England": "ENG",
    "Scotland": "SCO",
    "Wales": "WAL",
    "Northern Ireland": "NIR",
    "Saint-Martin": "MF",
    "Cape Verde": "CV",
    "The Gambia": "GM",
    "Chinese Taipei": "TW",
    "Curacao": "CW",
    "Kosovo": "XK",
    "Palestine": "PS",
    "St. Kitts & Nevis": "KN",
    "St. Lucia": "LC",
    "Neukaledonien": "NC",
    "Sint Maarten": "SX",
    "Tahiti": "PF",
    "Bonaire": "BQ",
    "Southern Sudan": "SS",
    "Turkey": "TR",
    "Russia": "RU",
}


def transform(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transforming data...")
    df = rename_columns(df)
    df = position_2_chars(df)
    df = sub_position_3_chars(df)
    df = nationality_2_chars(df)
    logger.info("Transformation completed successfully")
    return df


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Renaming columns...")
    df.rename(
        columns={
            "player_id": "id",
            "country_of_citizenship": "nationality",
        },
        inplace=True,
    )
    return df


def position_2_chars(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Renaming positions...")
    df.loc[df["position"] == "Attack", "position"] = "FW"
    df.loc[df["position"] == "Goalkeeper", "position"] = "GK"
    df.loc[df["position"] == "Defender", "position"] = "DF"
    df.loc[df["position"] == "Midfield", "position"] = "MD"
    df.loc[df["position"] == "Missing", "position"] = None
    return df


def sub_position_3_chars(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Renaming sub_positions...")
    # GK
    df.loc[df["sub_position"] == "Goalkeeper", "sub_position"] = "GK"

    # DF
    df.loc[df["sub_position"] == "Centre-Back", "sub_position"] = "CB"
    df.loc[df["sub_position"] == "Left-Back", "sub_position"] = "LB"
    df.loc[df["sub_position"] == "Right-Back", "sub_position"] = "RB"

    # MD
    df.loc[df["sub_position"] == "Defensive Midfield", "sub_position"] = "CDM"
    df.loc[df["sub_position"] == "Central Midfield", "sub_position"] = "MD"
    df.loc[df["sub_position"] == "Attacking Midfield", "sub_position"] = "CF"
    df.loc[df["sub_position"] == "Left Midfield", "sub_position"] = "LM"
    df.loc[df["sub_position"] == "Right Midfield", "sub_position"] = "RM"

    # FW
    df.loc[df["sub_position"] == "Left Winger", "sub_position"] = "LW"
    df.loc[df["sub_position"] == "Right Winger", "sub_position"] = "RW"
    df.loc[df["sub_position"] == "Second Striker", "sub_position"] = "SS"
    df.loc[df["sub_position"] == "Centre-Forward", "sub_position"] = "ST"

    df.loc[pd.isna(df["sub_position"]), "sub_position"] = None
    return df


def nationality_2_chars(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Renaming nationalities...")
    df["nationality"] = df["nationality"].apply(country_to_alpha2)
    return df


def country_to_alpha2(country_name):
    if pd.isna(country_name):
        return None
    if country_name in MANUAL_CORRECTIONS:
        return MANUAL_CORRECTIONS[country_name]
    try:
        return pycountry.countries.lookup(country_name).alpha_2
    except LookupError:
        return None
