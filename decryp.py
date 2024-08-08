
import os
from cryptography.fernet import Fernet as cryp

files=[]

link_folder=r"C:\Users\PC\OneDrive\Máy tính\Python (1)\test"

def find_file(link_path):
    try:
        for file in os.listdir(link_path):
            newlink=os.path.join(link_path,file)
            if os.path.isfile(newlink): 
                files.append(newlink)            
            else:
                find_file(newlink)                
    except :
        print(link_path)


def decryp_file(key_decrypt,files):
     for file in files:
        with open(file,"rb") as read:
            data=read.read()
        decrypted=cryp(key_decrypt).decrypt(data)
        with open(file,"wb") as write:
            write.write(decrypted)

find_file(link_folder)
#encryp_file(key,files)
with open(r"C:\Users\PC\OneDrive\Máy tính\Python (1)\key.key","rb") as thekey_decrypt:
    keydecrypt=thekey_decrypt.read()
    decryp_file(keydecrypt,files)