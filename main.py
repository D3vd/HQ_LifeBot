import string
import random
from pprint import pprint
import pyhq as hq


if __name__ == '__main__':

    phone_number = input("Phone Number : ")
    verification_id = hq.verify(phone_number)

    otp = input("OTP : ")
    sub_code_res = hq.submit_code(verification_id, otp)

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(6)) + ''.join(random.choice(string.digits) for _ in range(3))

    if hq.username_available(username):
        res = hq.create_user(username, verification_id)
    else:
        print("Try Again")

    pprint(res)
