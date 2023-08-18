from langchain import SerpAPIWrapper


def get_profile_url(text: str) -> str:
    """Searches for Linkedin Profile Page."""
    search = SerpAPIWrapper()
    return search.run(f"{text}")

