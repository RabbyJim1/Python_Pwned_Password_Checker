import requests
import hashlib


def request_api_data(quary_chars):
    url = "https://api.pwnedpasswords.com/range/" + quary_chars
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error Fetching: {response.status_code}, Check your url and try again!!!")
    return response

def get_password_leaks_counts(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        print(h, count)




def pwned_api_checker(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_5_char , tail = sha1_password[:5] , sha1_password[5:]
    print(first_5_char, tail)
    responses =  request_api_data(first_5_char)
    return get_password_leaks_counts(responses, tail)


print(pwned_api_checker("40408080"))


