#Câu 9
chuoi = input("Nhập vào chuỗi nhị phân: ")
if all(c in '01' for c in chuoi): 
    thap_phan = int(chuoi, 2)
    print(f"'{chuoi}' là số nhị phân, chuyển sang thập phân: {thap_phan}")
else:
    print(f"'{chuoi}' không phải là số nhị phân hợp lệ.")
