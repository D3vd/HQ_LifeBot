import requests
import string
import random
from pprint import pprint


class hq:

    def verify(phone: str) -> str:
        try:
            return requests.post("https://api-quiz.hype.space/verifications", data={
                "method": "sms",
                "phone": "+1" + phone
            }).json()["verificationId"]
        except KeyError:
            raise Exception("invalid phone number")

    def submit_code(verification_id: str, code: str) -> dict:
        return requests.post("https://api-quiz.hype.space/verifications/" + verification_id, data={"code": code}).json()

    def username_available(username: str) -> bool:
        return not bool(requests.post("https://api-quiz.hype.space/usernames/available", data={"username": username}).json())

    def create_user(username: str, verification_id: str, referral: str="", region: str="US", language: str="en"):
        return requests.post("https://api-quiz.hype.space/users", data={
            "country": region,
            "language": language,
            "referringUsername": referral,
            "username": username,
            "verificationId": verification_id
        }).json()


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
