#câu 12
# Nhập tử số và mẫu số
tu_so = int(input("Nhập vào tử số: "))
mau_so = int(input("Nhập vào mẫu số: "))

# Kiểm tra mẫu số phải là 0 hay không
if mau_so == 0:
    print("Mẫu số không thể bằng 0!")
else:
    # Tính ước chung lớn nhất
    a, b = tu_so, mau_so
    while b != 0:
        a, b = b, a % b
    
    # Tối giản phân số
    tu_so //= a
    mau_so //= a

    # In kết quả 
    print(f"Phân số đã tối giản là: {tu_so}/{mau_so}")