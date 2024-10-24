#Bài 4
import math 
#Nhập thời gian 
t_g = float(input("nhap thoi gian: "))

  #Điều kiện 
if t_g > 0: 
    #Các giá trị 
    U = 220 
    I = 2.7 
    #Tiền phải trả 
    tien_tra = U * I * t_g * 7000 / 3600 * 1000
    #In kết quả 
    print("tien phai tra: ", tien_tra)
else:
    print("thoi gian su dung phai lon hon 0") 