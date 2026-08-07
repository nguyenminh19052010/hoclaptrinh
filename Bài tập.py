import string
import random


#Bài 1
qua = ["Mũ", "Áo thun", "Balo", "Móc khóa", "Chúc bạn may mắn lần sau"]
chon = random.choice(qua)
print(chon)

#Bài 2
dem = len(string.punctuation)
print(dem)

#Bài 3
so = "09"
ds = string.digits
for i in range(8):
    so += random.choice(ds)
print(so)

#Bài 4
kho = string.ascii_lowercase
hoa = input("Bạn có muốn dùng chữ in HOA không? (y/n) ")
dac_biet = input("Bạn có muốn dùng ký tự đặc biệt không? (y/n) ")

if hoa.lower() == 'y':
    kho += string.ascii_uppercase
if dac_biet.lower() == 'y':
    kho += string.punctuation

print(kho)

#Bài 5
ten = input("Nhập tên: ")
so_duoi = ""
ds = string.digits
for i in range(3):
    so_duoi += random.choice(ds)
username = ten + so_duoi
print(username)

# Bài 6
dap_an = ["A. Hà Nội", "B. TP.HCM", "C. Đà Nẵng", "D. Cần Thơ"]
random.shuffle(dap_an)
print(dap_an)

#Bài 7
lua_chon = ["Kéo", "Búa", "Bao"]
may = random.choice(lua_chon)
nguoi = input("Nhập Kéo, Búa, hoặc Bao: ")

print("Máy chọn " + may + ", Người chọn " + nguoi)

if may == nguoi:
    print("Hòa")
elif (may == "Kéo" and nguoi == "Bao") or (may == "Búa" and nguoi == "Kéo") or (may == "Bao" and nguoi == "Búa"):
    print("Máy thắng")
else:
    print("Người thắng")

#Bài 8
mk = random.choice(string.ascii_lowercase)
mk += random.choice(string.ascii_uppercase)
mk += random.choice(string.digits)
print(mk)

#Bài 9
chuoi = input("Nhập chuỗi: ")
danh_sach = list(chuoi)
random.shuffle(danh_sach)
chuoi_moi = "".join(danh_sach)
print(chuoi_moi)

#Bài 10
mk10 = input("Nhập mật khẩu: ")
co_so = False
for ky_tu in mk10:
    if ky_tu in string.digits:
        co_so = True

if len(mk10) >= 8 and co_so == True:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")
