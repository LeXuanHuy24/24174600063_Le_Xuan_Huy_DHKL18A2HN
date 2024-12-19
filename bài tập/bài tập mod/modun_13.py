def phan_tich_thua_so_nguyen_to(n):
    if n <= 1:
        return f"Số {n} không hợp lệ để phân tích thành thừa số nguyên tố."
    thua_so = []
    while n % 2 == 0:
        thua_so.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            thua_so.append(i)
            n //= i
        i += 2  
    if n > 2:
        thua_so.append(n)

    return thua_so