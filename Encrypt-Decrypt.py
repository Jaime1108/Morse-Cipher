from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)
IV = get_random_bytes(AES.block_size) #Initialization Vector

cipher = AES.new(key, AES.MODE_CBC, IV)
plaintext = b'This is my super secret message to encrypt'

# Encrypting the plaintext
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
cipher_decrypt = AES.new(key, AES.MODE_CBC, IV)

# Decrypting the ciphertext
decrypted_data = unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
print(f"Decrypted message: {decrypted_data.decode()}")
