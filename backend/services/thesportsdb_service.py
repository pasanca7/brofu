import requests
import logging
import os

from backend.settings import THESPORTSDB_API_URL

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class ApiServiceError(Exception):
    """Base exception for API service errors."""

    pass


class ApiResponseError(ApiServiceError):
    """Exception for non-200 API responses."""

    def __init__(self, status_code, url, message="API returned non-200 status code"):
        self.status_code = status_code
        self.url = url
        self.message = message
        super().__init__(f"{self.message}: {self.status_code} for {self.url}")


class ApiResponseFormatError(ApiServiceError):
    """Exception for unexpected API response format (e.g., missing key or invalid JSON)."""

    def __init__(self, url, message="Unexpected API response format"):
        self.url = url
        self.message = message
        super().__init__(f"{self.message} from {self.url}")


def _handle_response(response: requests.Response, data_key: str):
    """
    Helper function to handle common API response processing.

    Args:
        response: The requests.Response object.
        data_key: The expected key in the JSON response containing the data list.

    Returns:
        A list of dictionaries (the data from the specified key).

    Raises:
        ApiResponseError: If the HTTP status code is not 200.
        ApiResponseFormatError: If the response is not valid JSON or the data_key is missing.
    """
    if response.status_code != 200:
        logging.error(f"API error: Status {response.status_code} for {response.url}")
        raise ApiResponseError(
            response.status_code, response.url, f"API call failed for {response.url}"
        )

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        logging.error(f"API error: Invalid JSON response from {response.url}")
        raise ApiResponseFormatError(
            response.url, f"Invalid JSON response from {response.url}"
        )

    # TheSportsDB often returns {"key": null} for no results, handle this
    if data_key not in data or data[data_key] is None:
        logging.info(
            f"API response: Key '{data_key}' not found or is null in response from {response.url}. Returning empty list."
        )
        return []  # Return empty list if key is missing or null

    # Ensure the data under the key is a list
    if not isinstance(data[data_key], list):
        logging.error(
            f"API error: Expected list under key '{data_key}' but got {type(data[data_key])} from {response.url}"
        )
        raise ApiResponseFormatError(
            response.url, f"Expected list under key '{data_key}'"
        )

    return data[data_key]


def get_leagues():
    response = requests.get(THESPORTSDB_API_URL + "/all_leagues.php")
    return _handle_response(response, "leagues")


def get_all_laliga_teams():
    response = requests.get(
        THESPORTSDB_API_URL + "/search_all_teams.php?l=Spanish%20La%20Liga"
    )
    return _handle_response(response, "teams")


def search_player_by_name(player_search: str):
    response = requests.get(
        THESPORTSDB_API_URL + "/searchplayers.php?p=" + player_search
    )
    return _handle_response(response, "player")


def get_contracts_by_player_id(player_id: int):
    response = requests.get(
        THESPORTSDB_API_URL + "/lookupcontracts.php?id=" + str(player_id)
    )
    return _handle_response(response, "contracts")


def get_former_teams_by_player_id(player_id: int):
    response = requests.get(
        THESPORTSDB_API_URL + "/lookupformerteams.php?id=" + str(player_id)
    )
    return _handle_response(response, "formerteams")
