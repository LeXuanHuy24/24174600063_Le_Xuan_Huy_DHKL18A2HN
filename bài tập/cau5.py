# 5. Viết chương trình kiểm tra một ký tự trong bảng chữ cái tiếng anh là nguyên âm hay phụ âm. 
# Ký tự là bất kỳ được nhập từ bàn phím.
char = input("Nhập một ký tự: ")

# Kiểm tra ký tự có phải là chữ cái không
if len(char) == 1 and char.isalpha():
    # Danh sách các nguyên âm
    vowels = "aeiouAEIOU"
    
    if char in vowels:
        print(f"Ký tự '{char}' là nguyên âm.")
    else:
        print(f"Ký tự '{char}' là phụ âm.")
else:
    print("Vui lòng nhập một ký tự hợp lệ.")