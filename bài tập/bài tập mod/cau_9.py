import modun_9
tu = int(input("bạn hãy nhập phần tử là : "))
mau = int(input("bạn hãy nhập phần mẫu là : "))
if mau == 0 :
    print("Kết quả của bạn là : 0 'xin hãy nhập lại >_<")
else :
    tu_toi_gian , mau_toi_gian = modun_9.phan_so_toi_giam(tu, mau)
    print(f"Kết quả của {tu}/{mau} là :    {tu_toi_gian}/{mau_toi_gian} ")
