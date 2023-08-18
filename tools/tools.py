from langchain import SerpAPIWrapper


class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

    @staticmethod
    def _process_response(res: dict) -> str:
        """Process response from SerpAPI"""
        return res["organic_results"][0]["link"]


def get_profile_url(text: str) -> str:
    """Searches for Linkedin Profile Page."""
    search = CustomSerpAPIWrapper()
    return search.run(f"{text}")
