#câu 7
import math

# Nhập vào giá trị n
n = int(input("Nhập một số nguyên dương n: "))

# Duyệt qua tất cả các số từ 2 đến n-1
for num in range(2, n):
    is_prime = True  # Giả sử num là số nguyên tố
    
    # Kiểm tra nếu num chia hết cho bất kỳ số nào từ 2 đến sqrt(num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False  # Nếu chia hết thì không phải số nguyên tố
            break
    
    # Nếu num là số nguyên tố, in ra num
    if is_prime:
        print(num, end=" ")
