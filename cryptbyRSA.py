from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os


def gen_key(link_path):
    # Tạo khóa RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,    
        key_size=2048,
        )

    # Lưu khóa riêng vào file
    with open(f"{link_path}/private_key.pem", "wb") as private_key_file:
        private_key_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()))

    # Lưu khóa công khai vào file
    public_key = private_key.public_key()
    with open(f"{link_path}/public_key.pem", "wb") as public_key_file:
        public_key_file.write(
            public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo))
    print("Khóa đã được tạo và lưu vào tệp.")    


#1GE=
def readkey():
    # Đọc khóa công khai từ file
        with open(r"C:\Users\PC\OneDrive\Máy tính\Python (1)\private_key.pem", "rb") as private_key_file:
         private_key = serialization.load_pem_private_key(private_key_file.read(),password=None)
         return private_key

def encryp_data(link_path,private_key):
# Mã hóa dữ liệu bằng khóa công khai
        with open(link_path,"rb") as read:
            data = read.read()
            decryped=private_key.decrypt(data,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        with open(link_path,"wb") as write:
             write.write(decryped)
        print("Dữ liệu đã được mã hóa:", link_path)



link_key=r"C:\Users\PC\OneDrive\Máy tính\Python (1)\key.key"
#gen_key(link_folder)
private_key=readkey()
encryp_data(link_key,private_key)




