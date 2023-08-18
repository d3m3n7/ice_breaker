import json
import os
import requests

from utils import save_to_file


def scrape_linkedin_profile(url: str) -> dict:
    """scrape information from LinkedIn profiles given the linkedin url"""
    assert url == "https://www.linkedin.com/in/johnrmarty"
    with open("./third_parties/linkedin_data/johnmarty.json", "r") as f:
        return filter_keys(json.loads(f.read()))


def filter_keys(d: dict) -> dict:
    relevant_keys = [
        "public_identifier",
        "first_name",
        "last_name",
        "follower_count",
        "headline",
        "experiences",
    ]
    return {key: d[key] for key in relevant_keys if key in d}


def test_request():
    """This will retrieve the John Marty linkedin profile, however it also consumes 1 Proxycurl token so use
    carefully."""
    api_key = os.environ.get("PROXYCURL_API_KEY")
    headers = {"Authorization": "Bearer " + api_key}
    endpoint = "http://nubela.co/proxycurl/api/v2/linkedin"
    params = {"url": "https://www.linkedin.com/in/johnrmarty/"}
    response = requests.get(url=endpoint, params=params, headers=headers)
    save_to_file(response.json(), file="test_request.json")
    return response.json()
