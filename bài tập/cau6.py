# 6. Viết chương trình thể hiện menu lựa chọn gồm các thể loại phim hiện đang có trong rạp chiếu phim ABC. 
# Yêu cầu người dùng nhập lựa chọn thể loại phim muốn xem (Phim tình cảm, Phim kinh dị, Phim hoạt hình, Phim khoa học viễn tưởng)
print("Chào mừng đến với rạp chiếu phim MOI!")
print("Xin mời bạn chọn loại phim: ")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")
print("0, Thoát")
while True:
    su_lua_chon = input("Nhap so tuong ung voi the loai phim bạn muon xem (0 de thoat): ")
    if su_lua_chon == '1':
        print("Bạn đã chọn : Phim tình cảm")
    elif su_lua_chon == '2':
        print("Bạn đã chọn : Phim kinh dị")
    elif su_lua_chon == '3':
        print("Bạn đã chọn : Phim hoạt hình")
    elif su_lua_chon == '4':
        print("Bạn đã chọm : Phim khoa học viễn tưởng")
    elif su_lua_chon == '0':
        print("Cảm ơn bạn đã đến và hẹn gặp lại!")
    else:
        print("Lựa chọn ko hợp lệ. Vui lòng nhập lại")