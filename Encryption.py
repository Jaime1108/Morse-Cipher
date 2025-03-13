from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

key = get_random_bytes(16)
IV = get_random_bytes(AES.block_size)
def Encryption(text):
    
    cipher = AES.new(key, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(pad(text,AES.block_size))
    return base64.b64encode(ciphertext).decode()
#ciphertext

original = "cyka-blyat asd asdafdsa casdfasdfac casdcasd"
text= original.encode()
print("original: ",original)
encrypted = Encryption(text)
print(encrypted)
decodedKey = base64.b64encode(key).decode()
decodedIV = base64.b64encode(IV).decode()
print(decodedKey)
print(decodedIV)