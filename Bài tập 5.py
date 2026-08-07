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

#bài 3    
danh_sach = []
for i in range(5):
    so_ngau_nhien = random.randint(0, 9)
    danh_sach.append(so_ngau_nhien)

print(danh_sach)

#bài 4 
do_dai = int(input("Nhập độ dài mật khẩu: "))

bat_buoc = [
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),
    random.choice(string.digits),
    random.choice(string.punctuation)      
]
kho_tu_do = string.ascii_letters + string.digits + string.punctuation
for i in range(do_dai - 4):
    bat_buoc.append(random.choice(kho_tu_do))

random.shuffle(bat_buoc)
mat_khau_hoan_chinh = "".join(bat_buoc)
print(f"Mật khẩu: {mat_khau_hoan_chinh}")

#bài 5
do_dai = int(input("Nhập độ dài mật khẩu: "))

if do_dai < 4:
    print("Cần ít nhất 4 ký tự!")
else:
    bat_buoc = [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase), random.choice(string.digits), random.choice(string.punctuation)]

    kho_tu_do = string.ascii_letters + string.digits + string.punctuation
    for i in range(do_dai - 4):
        bat_buoc.append(random.choice(kho_tu_do))
    
    random.shuffle(bat_buoc)
    mat_khau_hoan_chinh = "".join(bat_buoc)
    print(f"Mật khẩu: {mat_khau_hoan_chinh}")

#bài 6 
print("Các mật khẩu gợi ý:")
kho_ky_tu = string.ascii_letters + string.digits + string.punctuation

for i in range(1, 4):
    mat_khau_goi_y = ""
    for j in range(10):
        mat_khau_goi_y += random.choice(kho_ky_tu)
    print(f"{i}. {mat_khau_goi_y}")



