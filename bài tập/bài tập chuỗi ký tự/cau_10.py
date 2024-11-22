#Câu 10
chuoi = input("Nhập vào chuỗi ký tự: ")
so = ""
khong_so = ""
for c in chuoi:
    if c in '0123456789':
        so += c
    else:
        khong_so += c
ket_qua = so + khong_so
print("Kết quả:", ket_qua)
