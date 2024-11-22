#câu 9
# Nhập vào n
n = int(input("Nhập một số n: "))

# Duyệt qua tất cả các số từ 1 đến sqrt(n-1) và kiểm tra các số chính phương
for i in range(1, int(n ** 0.5) + 1):
    # In số chính phương i^2
    print(i * i, end=" ")

