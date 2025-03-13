from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
from Crypto.Util.Padding import pad, unpad
def Decryption(text, key, IV):
    key = base64.urlsafe_b64decode(key)
    IV = base64.urlsafe_b64decode(IV)
    text = base64.urlsafe_b64decode(text)
    cipherDecrypt = AES.new(key, AES.MODE_CBC, IV)
    ##decrypted_data = unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
    ciphertext = unpad(cipherDecrypt.decrypt(text),AES.block_size)
    return ciphertext.decode()
text = "yFX3S9wNsTy1bHCwJBsMy6hANw/qXkunNaxmPebq2d5BZco7/00KPWTkPrN6oA33"
key = "4/arfE7TEYoL0dzoGTdf2g=="
IV = "QoslNLP2N2TKmV9HWtA/Sw=="
text2 = "yVvKIUpD5eNrq6Hi3UkrX7rWlFF8klPOSmt0qWpAc9Y="
key2= "rf5x4-wG12M4hnfnbpWrRQ=="
IV2 = "aU-_iqQi36Pjyun689KSAQ=="
#decode_key = base64.b64decode(key)
print(Decryption(text2,key2,IV2))

##print(Decryption("Qk1vk439s31xDx5TgUGvElalpIQJLqn4qWNVSFbOwqBhpfQhXcsWWvKaWhClvOiF","bvo1fLNwOEwdpQ+BtnWdtA==","YdSMcGtnI/dNvLl06QBD6g=="))