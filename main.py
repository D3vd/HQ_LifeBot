import string
import random
from pprint import pprint
import pyhq as hq
import networking as n
import asyncio


def generate_account():

    phone_number = input("Phone Number : ")
    verification_id = hq.verify(phone_number)

    otp = input("OTP : ")
    sub_code_res = hq.submit_code(verification_id, otp)

    refferal_code = input("Refferal : ")

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(6)) + ''.join(random.choice(string.digits) for _ in range(3))

    if hq.username_available(username):
        res = hq.create_user(username, verification_id, refferal_code)
    else:
        print("Try Again")

    pprint(res)

    BEARER_TOKEN = res['authToken']

    # BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxNDc3MzU5LCJ1c2VybmFtZSI6Imh5ZWFsdDk0MSIsImF2YXRhclVybCI6Imh0dHBzOi8vZDJ4dTFoZG9taDNucnguY2xvdWRmcm9udC5uZXQvZGVmYXVsdF9hdmF0YXJzL1VudGl0bGVkLTFfMDAwM19yZWQucG5nIiwidG9rZW4iOm51bGwsInJvbGVzIjpbXSwiY2xpZW50IjoiIiwiZ3Vlc3RJZCI6bnVsbCwidiI6MSwiaWF0IjoxNTMwODM3NTg5LCJleHAiOjE1Mzg2MTM1ODksImlzcyI6Imh5cGVxdWl6LzEifQ.-8Giv3aTj0g-zItZb5lzlUt_hA1tRqcQLoi9NMrhvFU'

    return BEARER_TOKEN


def stimulate_play_game(BEARER_TOKEN):

    main_url = f"https://api-quiz.hype.space/shows/now?type="
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}", "x-hq-client": "Android/1.3.0"}

    response_data = asyncio.get_event_loop().run_until_complete(n.get_json_response(main_url, timeout=1.5, headers=headers))

    pprint(response_data)


if __name__ == '__main__':

    B = generate_account()

    stimulate_play_game(B)
