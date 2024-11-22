#Câu 6
chuoi = input("Nhập vào chuỗi ký tự: ")
if chuoi[0] == '-': 
    is_number = True
    for i in chuoi[1:]: 
        if i < '0' or i > '9':
            is_number = False
            break  
    if is_number:
        print("Chuỗi là số âm.")
    else:
        print("Chuỗi không phải là số âm.")
else:
    print("Chuỗi không phải là số âm.")
