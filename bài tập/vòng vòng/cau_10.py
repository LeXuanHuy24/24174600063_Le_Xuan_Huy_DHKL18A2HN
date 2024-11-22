#câu 10
# Nhập vào hai số từ người dùng
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Áp dụng thuật toán
while b != 0:
    a, b = b, a % b

# In kết quả
print(f"Ước chung lớn nhất của hai số là: {a}")
