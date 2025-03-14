from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import sys
from Crypto.Util.Padding import pad, unpad
def Decryption(text, key, IV):
    key = base64.urlsafe_b64decode(key)
    IV = base64.urlsafe_b64decode(IV)
    text = base64.urlsafe_b64decode(text)
    cipherDecrypt = AES.new(key, AES.MODE_CBC, IV)
    ##decrypted_data = unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
    ciphertext = unpad(cipherDecrypt.decrypt(text),AES.block_size)
    return ciphertext.decode()


if __name__ == "__main__":
    # Read arguments passed from PHP
    input_text = sys.argv[1]
    key = sys.argv[2]
    IV = sys.argv[3]

    print(Decryption(input_text,key,IV))
