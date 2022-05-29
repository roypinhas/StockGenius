import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

class AESCipher:

    BLOCK_SIZE=16
    pad = lambda self,s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)
    unpad = lambda self,s: s[:-ord(s[len(s) - 1:])]

    #password = input("Enter encryption password: ")


    def encrypt(self,raw, password):

        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        raw = self.pad(raw).encode("utf-8")
        iv = Random.new().read(AES.block_size)
        print(type(iv))
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        print(type(cipher.encrypt(raw)))
        return base64.b64encode(iv + cipher.encrypt(raw))


    def decrypt(self,enc, password):
        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(private_key, AES.MODE_CBC, IV=iv)
        return self.unpad(cipher.decrypt(enc[16:]))



a = AESCipher()
# First let us encrypt secret message
encrypted = a.encrypt("This is a secret message", '404')
print(encrypted)

# Let us decrypt using our original password
decrypted = a.decrypt(encrypted.decode('windows-1252'), '404')

print(bytes.decode(decrypted))