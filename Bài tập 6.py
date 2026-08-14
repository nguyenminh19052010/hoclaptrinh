import string
import random

# Bài 1
chu_thuong = string.ascii_lowercase
chu_hoa = string.ascii_uppercase
chu_so = string.digits
ky_tu_dac_biet = string.punctuation
tat_ca = chu_thuong + chu_hoa + chu_so + ky_tu_dac_biet
print(tat_ca)

# Bài 2
lst = ['P', 'y', 't', 'h', 'o', 'n']
chuoi = "".join(lst)
print(chuoi)

# Bài 3
do_dai = int(input())
mat_khau = "".join(random.choices(tat_ca, k=do_dai))
print("Mật khẩu:", mat_khau)

# Bài 4
list_so = []
for _ in range(5):
    list_so.append(random.randint(0, 9))
print(list_so)

# Bài 5
do_dai = int(input())
mk = [
    random.choice(chu_thuong),
    random.choice(chu_hoa),
    random.choice(chu_so),
    random.choice(ky_tu_dac_biet)
]
for _ in range(do_dai - 4):
    mk.append(random.choice(tat_ca))
random.shuffle(mk)
print("Mật khẩu:", "".join(mk))

# Bài 6
do_dai = int(input())
if do_dai < 4:
    print("Cần ít nhất 4 ký tự!")
else:
    mk = [
        random.choice(chu_thuong),
        random.choice(chu_hoa),
        random.choice(chu_so),
        random.choice(ky_tu_dac_biet)
    ]
    for _ in range(do_dai - 4):
        mk.append(random.choice(tat_ca))
    random.shuffle(mk)
    print("Mật khẩu:", "".join(mk))

# Bài 7
for i in range(1, 4):
    mk = "".join(random.choices(tat_ca, k=10))
    print(f"{i}. {mk}")

#bài 8
kho_sach = tat_ca
for c in "l1IO0":
    kho_sach = kho_sach.replace(c, "")
print("Mật khẩu:", "".join(random.choices(kho_sach, k=10)))

#bài 9
do_dai = int(input())
print("Mật khẩu:", "".join(random.choices(tat_ca, k=do_dai)))
if do_dai < 8:
    print("Độ mạnh: Yếu")
elif do_dai <= 11:
    print("Độ mạnh: Trung bình")
else:
    print("Độ mạnh: Mạnh")

#bài 10
do_dai = int(input())
if do_dai < 4:
    print("Cần ít nhất 4 ký tự!")
else:
    mk = [
        random.choice(chu_thuong),
        random.choice(chu_hoa),
        random.choice(chu_so),
        random.choice(ky_tu_dac_biet)
    ]
    for _ in range(do_dai - 4):
        mk.append(random.choice(tat_ca))
    random.shuffle(mk)
    print("Mật khẩu:", "".join(mk))
    if do_dai < 8:
        print("Độ mạnh: Yếu")
    elif do_dai <= 11:
        print("Độ mạnh: Trung bình")
    else:
        print("Độ mạnh: Mạnh")



