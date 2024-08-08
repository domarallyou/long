
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os
def readkey():
    # Đọc khóa riêng từ file
    with open(r"C:\Users\PC\OneDrive\Máy tính\Python (1)\private_key.pem", "rb") as private_key_file:
        private_key = serialization.load_pem_private_key(private_key_file.read(), password=None)
        return private_key


def decryp_data(link_path,private_key):
    # Giải mã dữ liệu bằng khóa riêng
    with open(link_path,"rb") as read:
        data = read.read()
        decrypted_data = private_key.decrypt(
        data,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    with open(link_path,"wb") as write:
             write.write(decrypted_data)
    print("Dữ liệu đã được giải mã:", link_path)

link_key=r"C:\Users\PC\OneDrive\Máy tính\Python (1)\key.key"
private_key=readkey()
decryp_data(link_key,private_key)