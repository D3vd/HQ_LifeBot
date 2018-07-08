import pyhq as hq
from pprint import pprint
import requests
from pyhq import HQClient

#auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxMjQ3MDczLCJ1c2VybmFtZSI6ImRldjAwNDM1NSIsImF2YXRhclVybCI6Imh0dHBzOi8vZDJ4dTFoZG9taDNucnguY2xvdWRmcm9udC5uZXQvZGVmYXVsdF9hdmF0YXJzL1VudGl0bGVkLTFfMDAwNF9nb2xkLnBuZyIsInRva2VuIjpudWxsLCJyb2xlcyI6W10sImNsaWVudCI6IiIsImd1ZXN0SWQiOm51bGwsInYiOjEsImlhdCI6MTUzMDI1NDU0OSwiZXhwIjoxNTM4MDMwNTQ5LCJpc3MiOiJoeXBlcXVpei8xIn0.TF7IS2r6laPVwTkfb5eUkkmuf7YR5iu-QmHsdUYJ1Io'
auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxMTQ1NDQyLCJ1c2VybmFtZSI6InBGb3gyOTMiLCJhdmF0YXJVcmwiOiJzMzovL2h5cGVzcGFjZS1xdWl6L2RlZmF1bHRfYXZhdGFycy9VbnRpdGxlZC0xXzAwMDNfcmVkLnBuZyIsInRva2VuIjpudWxsLCJyb2xlcyI6W10sImNsaWVudCI6IiIsImd1ZXN0SWQiOm51bGwsInYiOjEsImlhdCI6MTUzMTA0ODcwMSwiZXhwIjoxNTM4ODI0NzAxLCJpc3MiOiJoeXBlcXVpei8xIn0.bB4xUpsp3sT_riDyAVMTuF1Jy_blVOkyx1fXtHcXR0g'
# auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxNDc3MzU5LCJ1c2VybmFtZSI6Imh5ZWFsdDk0MSIsImF2YXRhclVybCI6Imh0dHBzOi8vZDJ4dTFoZG9taDNucnguY2xvdWRmcm9udC5uZXQvZGVmYXVsdF9hdmF0YXJzL1VudGl0bGVkLTFfMDAwM19yZWQucG5nIiwidG9rZW4iOm51bGwsInJvbGVzIjpbXSwiY2xpZW50IjoiIiwiZ3Vlc3RJZCI6bnVsbCwidiI6MSwiaWF0IjoxNTMwODM3NTg5LCJleHAiOjE1Mzg2MTM1ODksImlzcyI6Imh5cGVxdWl6LzEifQ.-8Giv3aTj0g-zItZb5lzlUt_hA1tRqcQLoi9NMrhvFU'
# auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxNTI0NTg5LCJ1c2VybmFtZSI6InRzZHVvZzA2NCIsImF2YXRhclVybCI6Imh0dHBzOi8vZDJ4dTFoZG9taDNucnguY2xvdWRmcm9udC5uZXQvZGVmYXVsdF9hdmF0YXJzL1VudGl0bGVkLTFfMDAwMF9ncmVlbi5wbmciLCJ0b2tlbiI6bnVsbCwicm9sZXMiOltdLCJjbGllbnQiOiIiLCJndWVzdElkIjpudWxsLCJ2IjoxLCJpYXQiOjE1MzA5NzgxMzQsImV4cCI6MTUzODc1NDEzNCwiaXNzIjoiaHlwZXF1aXovMSJ9.dPK182mjbblwHpw0oz7RCxjai54Y4nvQdIwchOcr-rE'
# auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIxNTQ2NTE1LCJ1c2VybmFtZSI6InF0b2N6cjY1MiIsImF2YXRhclVybCI6Imh0dHBzOi8vZDJ4dTFoZG9taDNucnguY2xvdWRmcm9udC5uZXQvZGVmYXVsdF9hdmF0YXJzL1VudGl0bGVkLTFfMDAwM19yZWQucG5nIiwidG9rZW4iOm51bGwsInJvbGVzIjpbXSwiY2xpZW50IjoiIiwiZ3Vlc3RJZCI6bnVsbCwidiI6MSwiaWF0IjoxNTMxMDM3MzczLCJleHAiOjE1Mzg4MTMzNzMsImlzcyI6Imh5cGVxdWl6LzEifQ.GOq9aqqgEWpDr2Q3tEIryQgf5s8x2_AWfwCu9NvOb9Y'


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

    # phone_number = input('Phone Number : ')
    # verification_id = hq.verify(phone_number)['verificationId']
    # otp = input("OTP : ")
    # sub_code_res = hq.submit_code(verification_id, otp)
    #
    # pprint(sub_code_res)

    test = HQClient(auth_token)
    res = test.search_users('dfgdifogdigdiogfjijg')
    pprint(res)

    # phone_number = input('Phone Number : ')
    # verification_id = hq.verify(phone_number)
    # pprint(verification_id)
