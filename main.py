import string
import random
from pprint import pprint
import pyhq as hq
from pyhq import HQClient
import networking as n
import asyncio
import requests


def generate_account():

    phone_number = input("Phone Number : ")
    try:
        verification_id = hq.verify(phone_number)["verificationId"]
    except KeyError:
        print('Enter a valid number!')
        return '', '', ''

    otp = input("OTP : ")
    sub_code_res = hq.submit_code(verification_id, otp)

    if 'error' in sub_code_res:
        print(sub_code_res['error'])
        return '', '', ''

    if sub_code_res['auth'] is not None:
        print("Sorry, this number is associated with {}".format(sub_code_res['auth']['username']))
        return '', '', ''

    referral_code = input("Referral : ")

    if hq.username_available(referral_code):
        print('Not a valid Referral Code!')
        return '', '', ''

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(6)) + ''.join(random.choice(string.digits) for _ in range(3))

    if hq.username_available(username):
        res = hq.create_user(username, verification_id, referral_code)
    else:
        print("Try Again")
        return '', '', ''

    auth_token = res['authToken']

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
        u, auth_token, r = l.split()

    # do something with data

    file.close()


if __name__ == '__main__':

    prompt = '\n> '
    print('Create Account - c \nStimulate Play Game - s\nQuit - q ')
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

        elif op == 'q':
            print('Quiting....')
            break

        else:
            print('Wrong option try again')
