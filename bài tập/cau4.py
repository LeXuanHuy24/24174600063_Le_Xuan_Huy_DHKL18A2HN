# 4. Viết chương trình nhập vào các số a, b, c, sau đó kiểm tra bộ ba số a, b, c vừa nhập vào 
# là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác vuông cân, tam giác đều 
# hay không phải là bộ ba cạnh của tam giác.
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))


sides = sorted([a, b, c])
a, b, c = sides[0], sides[1], sides[2]


if a + b > c:
    
    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or b == c:
        print("Đây là tam giác cân.")
    elif a**2 + b**2 == c**2:
        print("Đây là tam giác vuông.")
    elif a == b and a**2 + b**2 == c**2:
        print("Đây là tam giác vuông cân.")
    else:
        print("Đây là tam giác thường.")
else:
    print("Đây không phải là bộ ba cạnh của tam giác.")