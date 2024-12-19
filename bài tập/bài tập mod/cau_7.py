import modun_7
a = int(input("Nhập giá trị của a: "))
b = int(input("Nhập giá trị của b: "))
if a == 0 and b == 0:
    print("Bạn hãy nhập lại a và b vì cả hai không thể đồng thời bằng 0.")
else:
    ucln = modun_7.uclln(a, b)
    print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")
