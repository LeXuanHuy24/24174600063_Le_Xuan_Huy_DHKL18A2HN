#câu 14
# Chương trình vẽ tam giác Pascal và tam giác Floyd
# Tam giác pascal
# Nhập số hàng cho Tam giác Pascal
n = int(input("Nhập số hàng cho Tam giác Pascal: "))

# Tam giác Pascal
for i in range(n):
    # In khoảng trắng để căn giữa tam giác
    print(" " * (n - i), end="")

    # Tính và in giá trị trong hàng i
    tong = 1
    for j in range(i + 1):
        print(tong, end=" ")
        # Cập nhật giá trị tiếp theo trong hàng dựa trên hệ số nhị thức
        tong = tong * (i - j) // (j + 1)

    print()  # Xuống dòng 
#vẽ tam giác floyd
# Nhập số hàng cho Tam giác Floyd
n = int(input("Nhập số hàng cho Tam giác Floyd: "))

# Vẽ Tam giác Floyd
tong = 1  # Bắt đầu từ số 1
for i in range(1, n + 1):
    for j in range(i):
        print(tong, end=" ")
        tong =tong+ 1  # Tăng số sau mỗi lần in
    print()  #Xuống dòng