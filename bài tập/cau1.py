#1 tính năm nhuận. Năm thứ n là năm nhuận nếu chia hết cho 4, nhưng không chia hết cho 100 hoặc chia hết cho 400
a = int(input("Năm nay là năm :"))
if a % 4 == 0 and (a % 100 !=  0 or a % 400 != 0):
    print(f"{a} là năm nhuận")
else:
    print(f"{a} không phải là năm nhuận")
    