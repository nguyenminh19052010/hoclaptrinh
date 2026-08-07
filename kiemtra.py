#Bài 1

s = input("Nhập mật khẩu: ")
thuong = 0
hoa = 0
so = 0
dac_biet = 0

for c in s:
    if c.islower():
        thuong += 1
    elif c.isupper():
        hoa += 1
    elif c.isdigit():
        so += 1
    else:
        dac_biet += 1

print("Chữ cái thường:", thuong)
print("Chữ cái in HOA:", hoa)
print("Chữ số:", so)
print("Ký tự đặc biệt:", dac_biet)

#Bài 2

hovaten = input("Nhập họ và tên: ")
username = ""
for c in hovaten:
    if c.isupper():
        c = c.lower()
        username += c

print(username)

#Bài 3
sdt = input("Nhập số điện thoại: ")
sdt = sdt.replace(sdt[3:7], "****")
print(sdt)


#Bài 4
import random

hoc_sinh = ["An", "Bình", "Chi", "Dũng", "Giang", "Hương", "Khánh"]

chon = []

while len(chon) < 3:
    hs = random.choice(hoc_sinh)
    if hs not in chon:
        chon.append(hs)

print(chon)

#Bài 5

import random
import string

N = int(input("Nhập độ dài mật khẩu: "))

if N < 2:
    print("Độ dài mật khẩu phải lớn hơn hoặc bằng 2")
else:
    mat_khau = []

    mat_khau.append(random.choice(string.ascii_uppercase))
    mat_khau.append(random.choice(string.digits))

    for i in range(N-2):
        mat_khau.append(random.choice(string.ascii_lowercase))

    random.shuffle(mat_khau)
    mat_khau = "".join(mat_khau)

    print(mat_khau)