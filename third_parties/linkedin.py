import os
import requests

def scrape_linkedin_profile(url: str):
    """scrape information from LinkedIn profiles given the linkedin url"""


def test_request():
    api_key = os.environ.get('PROXYCURL_API_KEY')
    headers = {'Authorization': 'Bearer ' + api_key}
    endpoint = 'http://nubela.co/proxycurl/api/v2/linkedin'
    params = {
        'url': 'https://www.linkedin.com/in/johnrmarty/'
    }
    response = requests.get(url=endpoint,
                            params=params,
                            headers=headers)
    return response.json()
