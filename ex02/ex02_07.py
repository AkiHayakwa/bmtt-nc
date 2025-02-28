print("Nhap cac dong van ban (nhap 'q' de ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == 'q':
        break
    lines.append(line)

# In ra các dòng sau khi chuyển thành chữ in hoa
print("\nCac dong da nhap sau khi chuyen thanh chu in hoa :")
for line in lines:
    print(line.upper())
