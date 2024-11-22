# câu 15
# chuyển từ cơ số 10 sang cơ số 2
n = int(input("nhập hệ số thập phân: "))
if n == 0:
    print("số nhị phân là: 0 ")
else:
    # in các bit nhị phân từ phải sang trái
    while n > 0:
        print(n % 2, end="")
        n //= 2
    print() # xuống dòng

# chuyển từ cơ số 2 sang cơ số 10
b = input("nhập số nhị phân: ")
thap_phan = 0
for i in range(len(b)):
    thap_phan = thap_phan * 2 + int(b[i])
print(f"số thập phân là {thap_phan}")