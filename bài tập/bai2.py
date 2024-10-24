#Bài 2
#Tử Số = -x + (x**2+4)**(1/2)
#Mẫu só = (x**4+1)**(1/7)
#f_x= (-x + (x**2+4)**(1/2))/((x**4+1)**(1/7))
x = float(input("Nhập giá trị của x: "))
f_x = round((-x + (x**2+4)**(1/2))/((x**4+1)**(1/7)),2)
print(f"Giá trị của f(x) = {f_x}")
#không có điều kiện vì x ở mẫu mũ chẵn