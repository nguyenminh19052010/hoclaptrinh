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

#bài 4 (Bài 5 trong ảnh: Đảm bảo đủ 4 loại ký tự)
do_dai = int(input("Nhập độ dài mật khẩu: "))

# 1. Bắt buộc mỗi loại 1 ký tự
bat_buoc = [
    random.choice(string.ascii_lowercase),  # 1 chữ thường
    random.choice(string.ascii_uppercase),  # 1 chữ HOA
    random.choice(string.digits),           # 1 số
    random.choice(string.punctuation)       # 1 ký tự đặc biệt
]

# 2. Các ký tự còn lại chọn tự do từ kho tổng hợp
kho_tu_do = string.ascii_letters + string.digits + string.punctuation
for i in range(do_dai - 4):
    bat_buoc.append(random.choice(kho_tu_do))

# 3. Xáo trộn danh sách ký tự
random.shuffle(bat_buoc)

# 4. Nối lại thành chuỗi mật khẩu hoàn chỉnh
mat_khau_hoan_chinh = "".join(bat_buoc)
print(f"Mật khẩu: {mat_khau_hoan_chinh}")

#bài 5 (Bài 6 trong ảnh: Kiểm tra độ dài hợp lệ)
do_dai = int(input("Nhập độ dài mật khẩu: "))

if do_dai < 4:
    print("Cần ít nhất 4 ký tự!")
else:
    # 1. Bắt buộc mỗi loại 1 ký tự
    bat_buoc = [
        random.choice(string.ascii_lowercase),  # 1 chữ thường
        random.choice(string.ascii_uppercase),  # 1 chữ HOA
        random.choice(string.digits),           # 1 số
        random.choice(string.punctuation)       # 1 ký tự đặc biệt
    ]

    # 2. Các ký tự còn lại chọn tự do từ kho tổng hợp
    kho_tu_do = string.ascii_letters + string.digits + string.punctuation
    for i in range(do_dai - 4):
        bat_buoc.append(random.choice(kho_tu_do))

    # 3. Xáo trộn danh sách ký tự
    random.shuffle(bat_buoc)

    # 4. Nối lại thành chuỗi mật khẩu hoàn chỉnh
    mat_khau_hoan_chinh = "".join(bat_buoc)
    print(f"Mật khẩu: {mat_khau_hoan_chinh}")


