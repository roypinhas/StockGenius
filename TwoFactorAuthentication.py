import smtplib
import secrets
import hashlib
import hmac
import math
import time

class TwoFA:

    def send_email(self,message, rcv_email,sender_email, sender_password):
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(sender_email, sender_password)

        # sending the mail
        s.sendmail(sender_email, rcv_email, message)

        # terminating the session
        s.quit()

    def generate_shared_secret(self) -> str:
        return secrets.token_hex(16)
        # >> e8fb1a2faf331bfffe8670ca20447fae

    '''Convert the hash (base 16) into a binary string (base 2)
        Get the last four bits as an integer (base 10)
        Use this integer as an offset and get the next 32 bits of the binary string
        Convert this 32 bits to integer and get the last X digits,
        where X is the length you want to use'''

    def dynamic_truncation(self,raw_key: hmac.HMAC, length: int) -> str:
        bitstring = bin(int(raw_key.hexdigest(), base=16))

        last_four_bits = bitstring[-4:]

        offset = int(last_four_bits, base=2)

        chosen_32_bits = bitstring[offset * 8: offset * 8 + 32]

        full_totp = str(int(chosen_32_bits, base=2))

        return full_totp[-length:]


    #send this
    def generate_totp(self,shared_key: str, length: int = 6) -> str:
        now_in_seconds = math.floor(time.time())
        step_in_seconds = 60

        t = math.floor(now_in_seconds / step_in_seconds)
        hash = hmac.new(
            bytes(shared_key, encoding="utf-8"),
            t.to_bytes(length=8, byteorder="big"),
            hashlib.sha256,
        )

        return self.dynamic_truncation(hash, length)

    def validate_totp(self, totp: str, shared_key: str) -> bool:
        print("totp: " + str(totp) + " actual: " + str(self.generate_totp(shared_key)))
        return totp == self.generate_totp(shared_key)

    def fa(self,rcv_email,sender_email, sender_password):
        key = self.generate_shared_secret()
        totp = self.generate_totp(key)
        self.send_email(totp,rcv_email,sender_email, sender_password)
        inp = input("enter:")
        return self.validate_totp(inp,key)

'''
a = TwoFA()
print(a.fa())'''