#câu 8
# Nhập giá trị n
n = int(input("Nhập một số nguyên dương n: "))

# Duyệt tất cả các số từ 1 đến n-1
for num in range(1, n):
    tong_uoc = 0
    # Tìm ước số của num, ngoài chính nó
    for i in range(1, num):
        if num % i == 0:
            tong_uoc += i  # Cộng các ước số vào tổng
    
    # Kiểm tra xem tổng các ước số có bằng num không
    if tong_uoc == num:
        print(num, end=" ")
