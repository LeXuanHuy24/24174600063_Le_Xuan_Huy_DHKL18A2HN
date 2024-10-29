def kiem_tra_diem_trong_hinh_tron(x, y, a, b, R):
    # Tính khoảng cách từ điểm M đến tâm I
    khoang_cach = ((x - a) ** 2 + (y - b) ** 2) ** 0.5
    # Kiểm tra xem điểm M có nằm trong hoặc trên hình tròn không
    return khoang_cach <= R

# Nhập vào các giá trị từ bàn phím
x = float(input("Nhập hoành độ của điểm M (x): "))
y = float(input("Nhập tung độ của điểm M (y): "))
a = float(input("Nhập hoành độ của tâm I (a): "))
b = float(input("Nhập tung độ của tâm I (b): "))
R = float(input("Nhập bán kính R: "))

# Kiểm tra và in kết quả
if kiem_tra_diem_trong_hinh_tron(x, y, a, b, R):
    print("True - Điểm M nằm trong hoặc trên hình tròn.")
else:
    print("False - Điểm M nằm ngoài hình tròn.")
