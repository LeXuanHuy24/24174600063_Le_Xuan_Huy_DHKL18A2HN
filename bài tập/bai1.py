#bài 1
import math
    # Nhập bán kính và chều cao từ bàn phím
R  = float(input("nhap ban kinh (R): "))
H  = float(input("nhap chieu cao (H): "))
#điều kiện
if R > 0 and H > 0:
    pi = 3.14
    #Tính diện tích xung quanh, diện tích toàn phần và thể tích khối trụ
    Dien_tich_xung_quanh = 2 * math.pi * R * H 
    Dien_tich_toan_phan = 2 * math.pi * R * H +2 * pi * R**2
    the_tich = pi * R**2 * H
    
    # Kết quả
    print(f"dien tich xung quanh: {round(Dien_tich_xung_quanh, 2)} ")
    print(f"dien tich toàn phan: {round(Dien_tich_toan_phan, 2)}")
    print(f"the tich: {round(the_tich, 2)}")
else:
    print("R va H phai lon hon 0")