#Câu 4
chuoi = input("Nhập vào chuỗi ký tự: ")
so_chu = 0      
so_so = 0       
so_ky_tu_dac_biet = 0  
for ky_tu in chuoi:
    if ('a' <= ky_tu <= 'z') or ('A' <= ky_tu <= 'Z'):
        so_chu += 1
    elif '0' <= ky_tu <= '9':
        so_so += 1
    elif ky_tu != ' ':
        so_ky_tu_dac_biet += 1
print(f"Số ký tự là chữ: {so_chu}")
print(f"Số ký tự là số: {so_so}")
print(f"Số ký tự đặc biệt: {so_ky_tu_dac_biet}")
