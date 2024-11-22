#Câu 5
chuoi = input("Nhập vào chuỗi ký tự: ")
so_chu_hoa = 0 
so_chu_thuong = 0 
for ky_tu in chuoi:
    if 'A' <= ky_tu <= 'Z':
        so_chu_hoa += 1
    elif 'a' <= ky_tu <= 'z':
        so_chu_thuong += 1
print(f"Số chữ cái viết hoa: {so_chu_hoa}")
print(f"Số chữ cái viết thường: {so_chu_thuong}")
