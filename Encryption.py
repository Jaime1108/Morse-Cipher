from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def Encryption(text):
    key = get_random_bytes(16)
    IV = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(pad(text,AES.block_size))
    return base64.b64encode(ciphertext).decode()
#ciphertext

text = b'cyka-blyat asd asdafdsa casdfasdfac casdcasd'
print("original: ",text)
encrypted = Encryption(text)
print(encrypted)