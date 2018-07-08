import pyhq as hq
from pprint import pprint
import requests


# auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxMjQ3MDczLCJ1c2VybmFtZSI6ImRldjAwNDM1NSIsImF2YXRhclVybCI6Imh0dHBzOi8vZDJ4dTFoZG9taDNucnguY2xvdWRmcm9udC5uZXQvZGVmYXVsdF9hdmF0YXJzL1VudGl0bGVkLTFfMDAwNF9nb2xkLnBuZyIsInRva2VuIjpudWxsLCJyb2xlcyI6W10sImNsaWVudCI6IiIsImd1ZXN0SWQiOm51bGwsInYiOjEsImlhdCI6MTUzMDI1NDU0OSwiZXhwIjoxNTM4MDMwNTQ5LCJpc3MiOiJoeXBlcXVpei8xIn0.TF7IS2r6laPVwTkfb5eUkkmuf7YR5iu-QmHsdUYJ1Io'


def default_headers():
    return {
        "x-hq-client": "Android/1.7.2",
        "authorization": "Bearer " + auth_token,
        "user-agent": "okhttp/3.8.0"
    }


def search_users(user: str):
    response = requests.get("https://api-quiz.hype.space/users?q=" + user, headers=default_headers(), verify=True).json()
    return response


if __name__ == '__main__':

    phone_number = input('Phone Number : ')
    verification_id = hq.verify(phone_number)
    otp = input("OTP : ")
    sub_code_res = hq.submit_code(verification_id, otp)

    pprint(sub_code_res)
