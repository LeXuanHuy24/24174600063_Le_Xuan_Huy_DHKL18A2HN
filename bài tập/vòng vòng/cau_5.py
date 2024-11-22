#câu 5
# Nhập một số
n = int(input("Nhập một số: "))

# Kiểm tra số hoàn hảo
if n <= 1:
    print(f"{n} không phải là số hoàn hảo.")
else:
    tong = 0
    # Tìm các ước số của n, ngoài chính nó
    for i in range(1, n):
        if n % i == 0:
            tong += i  # Cộng các ước số vào tổng
    
    # Kiểm tra tổng các ước số có bằng n không
    if tong == n:
        print(f"{n} là số hoàn hảo.")
    else:
        print(f"{n} không phải là số hoàn hảo.")
