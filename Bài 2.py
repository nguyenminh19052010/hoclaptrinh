#Bài 1
ds = list(map(float, input("nhập dãy số: ").split()))
max = ds[0]
for so in ds:
    if so > max:
        so = max
print("số lớn nhất là: ", max)        
#Bài 2
ds = list(map(float, input("nhập dãy số: ").split()))
ds2 = []
for so in ds:
    if so % 2 == 0:
        ds2.append(so)
print(ds2)
#Bài 3
ds = list(map(float, input("nhập dãy số: ").split()))
sl = len(ds)
tb = sum(ds) / sl
print("trung bình cộng là: ", tb)