#câu 11
# Nhập hai số
a = int(input("Nhập vào số thứ nhất: "))
b = int(input("Nhập vào số thứ hai: "))

# Tính ước chung lớn nhất
x, y = a, b
while y != 0:
    x, y = y, x % y

# In
print(f"Bội chung nhỏ nhất của {a} và {b} là: {abs(a * b) // x}")
