import requests


def get_webpage(url) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f'Failed to retrieve content. Status code: {response.status}')


def save_to_file(input: str, file: str):
    with open(file=file, mode='w') as f:
        f.write(input)
