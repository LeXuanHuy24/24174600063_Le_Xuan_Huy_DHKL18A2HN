#Viết chương trình kiểm tra xem điểm M(x,y) có nằm trong hình tròn tâm I(a,b) và bán kính 
# R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn và False nếu nằm ngoài hình tròn, 
# với x, y, a, b, R nhập vào từ bàn phím
# Nhập các giá trị
import math
x = float(input(" Nhập hoành độ của điểm M (x): "))
y = float(input("Nhập tung độ của điểm M (y): "))
a = float(input("Nhập hoành độ của điểm I (a): "))
b = float(input("Nhập tung độ của điểm I (b): "))
R = float(input("Nhập bán kính R: "))
khoang_cach = math.sqrt((x - a) ** 2 + (y - b) ** 2)
if khoang_cach <= R:
    print("true")
else:
    print("false")