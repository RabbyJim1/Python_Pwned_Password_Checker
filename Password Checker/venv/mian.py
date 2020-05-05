import requests


def request_api_data(quary_chars):
    url = "https://api.pwnedpasswords.com/range/" + quary_chars
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error Fetching: {response.status_code}, Check your url and try again!!!")
    return response


request_api_data("C7137")
