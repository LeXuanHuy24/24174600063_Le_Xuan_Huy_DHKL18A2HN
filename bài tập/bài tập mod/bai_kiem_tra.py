products  = []

while True:
    print("\nChọn chức năng:")
    print("1. Xem danh sách mặt hàng")
    print("2. Nhập thông tin mặt hàng")
    print("3. Tính thành tiền và thuế VAT")
    print("4. Tìm kiếm và xóa mặt hàng theo mã")
    print("5. Tìm kiếm và chỉnh sửa thông tin mặt hàng theo mã")
    print("6. Xem danh sách mặt hàng sắp xếp theo tên")
    print("7. Thoát")
    choice = input("Lựa chọn của bạn: ")

    try:
        if choice == "1":
            if not products:
                raise ValueError("Hiện không có mặt hàng nào.")
            print("Danh sách các mặt hàng:")
            for product in products:
                print(product)
 # Nhập thông tin mặt hàng
        elif choice == "2":
            product = {}
            product["ma_hang"] = input("Nhập mã hàng: ")
            if not product["ma_hang"]:
                raise ValueError("Mã hàng không được để trống.")
            
            product["ten_hang"] = input("Nhập tên hàng: ")
            if not product["ten_hang"]:
                raise ValueError("Tên hàng không được để trống.")
            
            product["don_vi_tinh"] = input("Nhập đơn vị tính: ")
            if not product["don_vi_tinh"]:
                raise ValueError("Đơn vị tính không được để trống.")
            
            product["don_gia"] = float(input("Nhập đơn giá: "))
            if product["don_gia"] <= 0:
                raise ValueError("Đơn giá phải lớn hơn 0.")
            
            product["so_luong"] = int(input("Nhập số lượng: "))
            if product["so_luong"] <= 0:
                raise ValueError("Số lượng phải lớn hơn 0.")
            
            product["thanh_tien"] = product["don_gia"] * product["so_luong"]
            product["thue_vat"] = product["thanh_tien"] * 0.1
            products.append(product)
            print("Đã thêm mặt hàng thành công.")
# Tính toán thành tiền và thuế VAT (nếu cần cập nhật)
        elif choice == "3":
            if not products:
                raise ValueError("Hiện không có mặt hàng nào để tính toán.")
            print("Cập nhật thành tiền và thuế VAT:")
            for product in products:
                product["thanh_tien"] = product["don_gia"] * product["so_luong"]
                product["thue_vat"] = product["thanh_tien"] * 0.1
                print(f"{product['ten_hang']} - Thành tiền: {product['thanh_tien']}, Thuế VAT: {product['thue_vat']}")
 # Tìm kiếm và xóa mặt hàng
        elif choice == "4":
            code = input("Nhập mã hàng cần xóa: ")
            found = False
            for product in products:
                if product["ma_hang"] == code:
                    products.remove(product)
                    print("Đã xóa mặt hàng thành công.")
                    found = True
                    break
            if not found:
                raise ValueError("Không tìm thấy mặt hàng với mã đã nhập.")
# Tìm kiếm và chỉnh sửa mặt hàng
        elif choice == "5":
            code = input("Nhập mã hàng cần sửa: ")
            found = False
            for product in products:
                if product["ma_hang"] == code:
                    print("Thông tin mặt hàng hiện tại:", product)
                    new_name = input("Nhập tên mới (bấm Enter để giữ nguyên): ")
                    new_unit = input("Nhập đơn vị tính mới (bấm Enter để giữ nguyên): ")
                    new_price = input("Nhập đơn giá mới (bấm Enter để giữ nguyên): ")
                    new_quantity = input("Nhập số lượng mới (bấm Enter để giữ nguyên): ")

                    if new_name:
                        product["ten_hang"] = new_name
                    if new_unit:
                        product["don_vi_tinh"] = new_unit
                    if new_price:
                        product["don_gia"] = float(new_price)
                    if new_quantity:
                        product["so_luong"] = int(new_quantity)

                    product["thanh_tien"] = product["don_gia"] * product["so_luong"]
                    product["thue_vat"] = product["thanh_tien"] * 0.1
                    print("Đã cập nhật thông tin mặt hàng.")
                    found = True
                    break
            if not found:
                raise ValueError("Không tìm thấy mặt hàng với mã đã nhập.")
# Xem danh sách mặt hàng sắp xếp theo tên
        elif choice == "6":
            if not products:
                raise ValueError("Hiện không có mặt hàng nào.")
            sorted_products = sorted(products, key=lambda x: x["ten_hang"])
            print("Danh sách mặt hàng sắp xếp theo tên:")
            for product in sorted_products:
                print(product)

        # Thoát chương trình
        elif choice == "7":
            print("Thoát chương trình.")
            break

        # Lựa chọn không hợp lệ
        else:
            raise ValueError("Lựa chọn không hợp lệ. Vui lòng thử lại.")
    
    except ValueError as e:
        print(f"Lỗi: {e}")
