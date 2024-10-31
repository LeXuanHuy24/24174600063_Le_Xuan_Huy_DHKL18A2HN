# 10. Viết chương trình nhập lương nhân viên, tính thuế thu nhập và lương ròng (số tiền
# lương thực sự mà nhân viên đó nhận được).
# Với các thông số giả sử như sau
# • 30% thuế thu nhập nếu lương là 15 triệu.
# • 20% thuế thu nhập nếu lương từ 7 đến 15 triệu.
# • 10% thuế thu nhập nếu lương dưới 7 triệu.
luong = float(input("Nhập số lương: (VNĐ)"))
if luong < 0:
    print("số lương ko đc âm")
else:
    if luong > 15000000:
       thue = luong * 0.30
    elif luong <= 15000000 and luong >= 7000000:
        thue = luong * 0.20
    else: 
        thue = luong * 0.10
#Tính lương ròng
luong_rong = luong - thue

#In 
print(f"\nLuong: {luong:.0f} VND")
print(f"Thuế: {thue:.0f} VND")
print(f"lương ròng: {luong_rong:.0f} VND")