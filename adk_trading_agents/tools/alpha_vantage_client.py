# adk_trading_agents/tools/alpha_vantage_client.py
import os
import requests
import json

API_BASE_URL = "https://www.alphavantage.co/query"

class AlphaVantageRateLimitError(Exception):
    """Exception raised when Alpha Vantage API rate limit is exceeded."""
    pass

def get_api_key() -> str:
    """Retrieve the API key for Alpha Vantage from environment variables."""
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not api_key:
        raise ValueError("ALPHA_VANTAGE_API_KEY environment variable is not set.")
    return api_key

def make_api_request(function_name: str, params: dict) -> dict | str:
    """Helper function to make API requests and handle responses."""
    api_params = params.copy()
    api_params.update({
        "function": function_name,
        "apikey": get_api_key(),
    })

    response = requests.get(API_BASE_URL, params=api_params)
    response.raise_for_status()

    response_text = response.text

    try:
        response_json = json.loads(response_text)
        if "Information" in response_json:
            info_message = response_json["Information"]
            if "rate limit" in info_message.lower() or "api key" in info_message.lower():
                raise AlphaVantageRateLimitError(f"Alpha Vantage rate limit exceeded: {info_message}")
    except json.JSONDecodeError:
        pass

    return response_text
