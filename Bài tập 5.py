import string
import random

#bài 1
lst = ['P', 'y', 't', 'h', 'o', 'n']
chuoi = "".join(lst)
print(chuoi)

#bài 2
do_dai = int(input("Nhập độ dài mật khẩu: "))

kho_ky_tu = string.ascii_letters + string.digits + string.punctuation

mat_khau = ""
for i in range(do_dai):
    mat_khau += random.choice(kho_ky_tu)

print(f"Mật khẩu: {mat_khau}")
        
danh_sach = []
for i in range(5):
    so_ngau_nhien = random.randint(0, 9)
    danh_sach.append(so_ngau_nhien)

print(danh_sach)
