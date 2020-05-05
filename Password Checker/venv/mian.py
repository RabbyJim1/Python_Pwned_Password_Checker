import requests
import hashlib


def request_api_data(quary_chars):
    url = "https://api.pwnedpasswords.com/range/" + quary_chars
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error Fetching: {response.status_code}, Check your url and try again!!!")
    return response


def pwned_api_checker(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return sha1_password

print(pwned_api_checker("40408080"))


