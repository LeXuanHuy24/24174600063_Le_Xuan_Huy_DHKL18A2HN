#câu 6
import math

# Nhập một số 
n = int(input("Nhập một số: "))

# Kiểm tra số chính phương
if n < 0:
    print(f"{n} không phải là số chính phương vì nó là số âm.")
else:
    # Tính căn bậc hai của n
    can_bac_2 = math.sqrt(n)

    # Kiểm tra nếu căn bậc hai là một số nguyên
    if can_bac_2.is_integer():
        print(f"{n} là số chính phương.")
    else:
        print(f"{n} không phải là số chính phương.")
