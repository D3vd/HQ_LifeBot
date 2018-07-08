import string
import random
from pprint import pprint
import pyhq as hq
import networking as n
import asyncio
import requests


def generate_account():

    phone_number = input("Phone Number : ")
    verification_id = hq.verify(phone_number)

    otp = input("OTP : ")
    sub_code_res = hq.submit_code(verification_id, otp)

    if sub_code_res['auth'] is not None:
        print("Sorry, this number is associated with {}".format(sub_code_res['auth']['username']))
        return '', '', ''

    referral_code = input("Referral : ")

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(6)) + ''.join(random.choice(string.digits) for _ in range(3))

    if hq.username_available(username):
        res = hq.create_user(username, verification_id, referral_code)
    else:
        print("Try Again")
        return '', '', ''

    auth_token = res['authToken']

    # BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxNDc3MzU5LCJ1c2VybmFtZSI6Imh5ZWFsdDk0MSIsImF2YXRhclVybCI6Imh0dHBzOi8vZDJ4dTFoZG9taDNucnguY2xvdWRmcm9udC5uZXQvZGVmYXVsdF9hdmF0YXJzL1VudGl0bGVkLTFfMDAwM19yZWQucG5nIiwidG9rZW4iOm51bGwsInJvbGVzIjpbXSwiY2xpZW50IjoiIiwiZ3Vlc3RJZCI6bnVsbCwidiI6MSwiaWF0IjoxNTMwODM3NTg5LCJleHAiOjE1Mzg2MTM1ODksImlzcyI6Imh5cGVxdWl6LzEifQ.-8Giv3aTj0g-zItZb5lzlUt_hA1tRqcQLoi9NMrhvFU'
    # BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxNTI0NTg5LCJ1c2VybmFtZSI6InRzZHVvZzA2NCIsImF2YXRhclVybCI6Imh0dHBzOi8vZDJ4dTFoZG9taDNucnguY2xvdWRmcm9udC5uZXQvZGVmYXVsdF9hdmF0YXJzL1VudGl0bGVkLTFfMDAwMF9ncmVlbi5wbmciLCJ0b2tlbiI6bnVsbCwicm9sZXMiOltdLCJjbGllbnQiOiIiLCJndWVzdElkIjpudWxsLCJ2IjoxLCJpYXQiOjE1MzA5NzgxMzQsImV4cCI6MTUzODc1NDEzNCwiaXNzIjoiaHlwZXF1aXovMSJ9.dPK182mjbblwHpw0oz7RCxjai54Y4nvQdIwchOcr-rE'
    # BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxNTQ2NTE1LCJ1c2VybmFtZSI6InF0b2N6cjY1MiIsImF2YXRhclVybCI6Imh0dHBzOi8vZDJ4dTFoZG9taDNucnguY2xvdWRmcm9udC5uZXQvZGVmYXVsdF9hdmF0YXJzL1VudGl0bGVkLTFfMDAwM19yZWQucG5nIiwidG9rZW4iOm51bGwsInJvbGVzIjpbXSwiY2xpZW50IjoiIiwiZ3Vlc3RJZCI6bnVsbCwidiI6MSwiaWF0IjoxNTMxMDM3MzczLCJleHAiOjE1Mzg4MTMzNzMsImlzcyI6Imh5cGVxdWl6LzEifQ.GOq9aqqgEWpDr2Q3tEIryQgf5s8x2_AWfwCu9NvOb9Y'

    return username, auth_token, referral_code


def write_data(u, a, r):

    file = open('data.txt', 'a')
    file.write('{} {} {}\n'.format(u, a, r))
    file.close()


def show_active():

    url = 'https://api-quiz.hype.space/shows/now'
    response = requests.get(url).json()
    return response['active']


def get_socket_url(token):

    main_url = f"https://api-quiz.hype.space/shows/now?type="
    headers = {"Authorization": f"Bearer {token}", "x-hq-client": "Android/1.3.0"}

    response_data = asyncio.get_event_loop().run_until_complete(n.get_json_response(main_url, timeout=1.5, headers=headers))

    pprint(response_data)

    socket_url = response_data['broadcast']['socketUrl'].replace("https", "wss")

    return socket_url


def get_socket_url():

    main_url = 'https://api-quiz.hype.space/shows/now'
    response_data = requests.get(main_url)

    socket_url = response_data['broadcast']['socketUrl'].replace("https", "wss")
    return socket_url


def read_data(url):

    file = open('data.txt', 'r')
    for l in file.readlines():
        u, a, r = l.split()

    # do something with data

    file.close()


if __name__ == '__main__':

    prompt = '\n> '
    print('Create Account - c \nStimulate Play Game - s ')
    op = ''

    while op != 'q':

        op = input(prompt)

        if op == 'c':

            username, token, referral = generate_account()

            if username != '':
                write_data(username, token, referral)
                print('Account with name {} created successfully!'.format(username))

        elif op == 's':

            if not show_active():
                print('The show not active, Try again!')
                continue

            url = get_socket_url()

            read_data(url)

        else:
            print('Wrong option try again')






