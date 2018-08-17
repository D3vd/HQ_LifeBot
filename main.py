import pyhq as hq
import requests
from lomond import WebSocket
from username_generator import create_username


def generate_account():

    phone_number = input("Phone Number : ")
    try:
        verification_id = hq.verify(phone_number)["verificationId"]
    except KeyError:
        print('Enter a valid number!')
        return '', '', ''

    code = input("Code : ")
    sub_code_res = hq.submit_code(verification_id, code)

    if 'error' in sub_code_res:
        print(sub_code_res['error'])
        return '', '', ''

    if sub_code_res['auth'] is not None:
        print("Sorry, this number is already associated with {}".format(sub_code_res['auth']['username']))
        return '', '', ''

    referral_code = input("Referral : ")

    if hq.username_available(referral_code):
        print('Not a valid Referral Code!')
        return '', '', ''

    # user_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(6)) + ''.join(random.choice(string.digits) for _ in range(3))

    user_name = create_username()

    if hq.username_available(user_name):
        res = hq.create_user(user_name, verification_id, referral_code)
    else:
        print("Try Again")
        return '', '', ''

    auth_token = res['authToken']

    return user_name, auth_token, referral_code


def write_data(u, a, r):

    file = open('data.txt', 'a')
    file.write('{} {} {}\n'.format(u, a, r))
    file.close()

    backup_file = open('backup.txt', 'a')
    backup_file.write('{} {} {}\n'.format(u, a, r))
    backup_file.close()


def show_active():

    main_url = 'https://api-quiz.hype.space/shows/now'
    response = requests.get(main_url).json()
    return response['active']


def get_socket_url():

    main_url = 'https://api-quiz.hype.space/shows/now'
    response_data = requests.get(main_url).json()

    socket_url = response_data['broadcast']['socketUrl'].replace("https", "wss")
    return socket_url


def read_data(socket_url):

    file = open('data.txt', 'r')
    for l in file.readlines():
        u, auth_token, r = l.split()

        status = connect_websocket(socket_url, auth_token)

        if status:
            print('Successfully created life for {} with username {}'.format(r, u))
        else:
            print('Unknown problem while creating life for {}'.format(r))

    file.close()
    delete_data()


def delete_data():
    f = open('data.txt', 'r+')
    f.truncate()


def connect_websocket(socket_url, auth_token):

    headers = {"Authorization": f"Bearer {auth_token}",
               "x-hq-client": "Android/1.3.0"}
    websocket = WebSocket(socket_url)
    cnt = 0
    try:
        for header, value in headers.items():
            websocket.add_header(str.encode(header), str.encode(value))
        for event in websocket.connect(ping_rate=5):
            if 'interaction' in str(event):
                cnt += 1
            if cnt > 5:
                websocket.close()
    except:
        return False

    return True


if __name__ == '__main__':

    prompt = '\n> '
    print('Create Account - c \nStimulate Game - s\nQuit - q ')
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
            print("Connecting to socket : " + url)

            read_data(url)

            print('\nSuccessfully created lives....')

        elif op == 'q':
            print('Quitting....')
            break

        else:
            print('Wrong option try again')
