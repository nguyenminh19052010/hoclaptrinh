
s = input("Nhập chuỗi: ")
print(s[::-1])


s = input()
print(s[:3])
 


thong_tin = input()
ten, tuoi = thong_tin.split(",")
ten = ten.strip()
tuoi = tuoi.strip()
print(f"Mình tên là {ten}, năm nay {tuoi} tuổi.")


s = input()
ten = " ".join(s.split()).title()
print(ten)


ky_hieu = input("Nhập ký hiệu: ")
n = int(input("Nhập số lần lặp: "))
print(ky_hieu * n)


# Bài 9: Tạo chữ cái viết tắt (initials)
ten1 = input().strip()
ten2 = input().strip()
viet_tat = f"{ten1[0].upper()}.{ten2[0].upper()}"
print(viet_tat)


# Bài 10: Máy tạo tên siêu anh hùng
thong_tin = input()
mau, con_vat = thong_tin.split(",")
mau = mau.strip().capitalize()
con_vat = con_vat.strip().capitalize()
print(f"⚡ Biệt danh của bạn: {mau} {con_vat} Huyền Thoại")


import random
import string

s = string.ascii_lowercase  
ky_tu = random.choice(s)
print(ky_tu)

otp = ""
for i in range(6):
    otp += random.choice(string.digits)

print("OTP:", otp)


# Bài 6: Xáo trộn danh sách
danh_sach = ["An", "Bình", "Cường", "Lan"]
random.shuffle(danh_sach)
print(danh_sach)


# Bài 7: Mật khẩu ngẫu nhiên 4 ký tự (dùng vòng lặp for)
mat_khau = ""
for i in range(4):
    mat_khau += random.choice(string.ascii_lowercase)

print(mat_khau)


so = ""
for i in range(4):
    so += random.choice("0123456789")

ma_giam_gia = "SALE" + so
print(ma_giam_gia)



import random
import string

n = int(input("Nhập độ dài mật khẩu: "))

kho_ky_tu = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
mat_khau = ""

for i in range(n):
    mat_khau += random.choice(kho_ky_tu)

print("Mật khẩu:", mat_khau)



cam_xuc = input("Bạn đang buồn hay vui? ").strip().lower()

hoat_dong_buon = ["Đi dạo hít thở không khí","Nghe nhạc nhẹ nhàng","Xem một bộ phim hài giải trí","Nghỉ ngơi thư giãn","Đi ăn món mình thích"]

hoat_dong_vui = ["Đi đạp xe cùng bạn bè","Tụ tập đi cà phê tán tán chuyện","Hát karaoke","Thử học một điều mới lạ","Chụp ảnh check-in"]

if cam_xuc == "buồn":
    goi_y = random.choice(hoat_dong_buon)
elif cam_xuc == "vui":
    goi_y = random.choice(hoat_dong_vui)
else:
    goi_y = random.choice(hoat_dong_buon + hoat_dong_vui)

print("Gợi ý cho bạn:", goi_y)



