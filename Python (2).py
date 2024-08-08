import pandas as pd
import unidecode
import random
import string


def read_first_column_excel(file_path):
    try:
        # Đọc file Excel vào DataFrame
        df = pd.read_excel(file_path, engine='openpyxl')
        # Lấy cột đầu tiên
        first_column = df.iloc[:, 0].tolist()
        return first_column
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []
    
def convert_name(name):
    # Chuyển thành chữ thường
    lower_case = name.lower()
    # Loại bỏ dấu
    no_diacritics = unidecode.unidecode(lower_case)
    # Loại bỏ khoảng trắng
    no_spaces = no_diacritics.replace(" ", "")
    return no_spaces


def generate_random_string(length=8):
    # Chọn từ các ký tự chữ cái và chữ số
    characters = string.ascii_letters + string.digits
    # Tạo dãy ngẫu nhiên với độ dài cho trước
    random_string = ''.join(random.choice(characters) for _ in range(length)).strip()
    return random_string


def write_to_first_column(file_path, new_data,passlist):
    # Tạo DataFrame với dữ liệu mới cho cột đầu tiên
    df = pd.DataFrame({
        'Name':new_data,
        'pass':passlist
    })
    # Ghi DataFrame vào file Excel
    df.to_excel(file_path, index=False, engine='openpyxl')


file_path=r"C:\Users\PC\OneDrive\Máy tính\Python (1)\Python (1).xlsx"
file_path1=r"C:\Users\PC\OneDrive\Máy tính\Python (1)\Python (2).xlsx"
listname= read_first_column_excel(file_path)
listpass=[]

for i in range(len(listname)):
    listpass.append(generate_random_string())

converted_names = [convert_name(name) for name in listname]
write_to_first_column(file_path1,converted_names,listpass)





