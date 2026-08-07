import string
import random

# ==========================================
# Bài 2: Ghép list thành chuỗi
# ==========================================
lst = ['P', 'y', 't', 'h', 'o', 'n']
chuoi = "".join(lst)
print("Bài 2 - Kết quả:")
print(chuoi)
print("-" * 30)

# ==========================================
# Bài 3: Mật khẩu theo độ dài chọn
# ==========================================
do_dai = int(input("Bài 3 - Nhập độ dài mật khẩu: "))

# Kho ký tự đầy đủ: chữ thường + chữ hoa + chữ số + ký tự đặc biệt
kho_ky_tu = string.ascii_letters + string.digits + string.punctuation

mat_khau = ""
for i in range(do_dai):
    mat_khau += random.choice(kho_ky_tu)

print(f"Mật khẩu: {mat_khau}")
print("-" * 30)

# ==========================================
# Bài 4: Thêm ký tự vào list
# ==========================================
danh_sach = []
for i in range(5):
    so_ngau_nhien = random.randint(0, 9)
    danh_sach.append(so_ngau_nhien)

print("Bài 4 - Kết quả (list 5 số ngẫu nhiên từ 0-9):")
print(danh_sach)
