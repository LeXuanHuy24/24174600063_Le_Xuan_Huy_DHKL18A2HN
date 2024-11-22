#câu 4
# Nhập một số
n = int(input("Nhập vào một số: "))

# Kiểm tra số nguyên tố
if n <= 1:
    print(f"{n} không phải là số nguyên tố.")
else:
    for i in range(2, n):  # Kiểm tra từ 2 đến n-1
        if n % i == 0:  # Nếu n chia hết cho i, thì n không phải số nguyên tố
            print(f"{n} không phải là số nguyên tố.")
            break  # Ngừng kiểm tra nếu đã tìm thấy chia hết
    else:
        print(f"{n} là số nguyên tố.")
