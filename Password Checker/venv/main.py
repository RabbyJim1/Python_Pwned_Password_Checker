import requests
import hashlib
import sys

def request_api_data(quary_chars):
    url = "https://api.pwnedpasswords.com/range/" + quary_chars
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error Fetching: {response.status_code}, Check your url and try again!!!")
    return response

def get_password_leaks_counts(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_checker(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_5_char , tail = sha1_password[:5] , sha1_password[5:]
    responses =  request_api_data(first_5_char)
    return get_password_leaks_counts(responses, tail)

def main(args):
    for password in args:
        count = pwned_api_checker(password)
        if count:
            print(f"{password} was found {count} times. Change your password!!!")
        else:
            print(f"{password} was not found. Congraculation! Your password is secured.")

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
