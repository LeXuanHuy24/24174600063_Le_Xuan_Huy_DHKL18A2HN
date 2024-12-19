def danh_sach_uoc_so_nguyen(n):
    uoc = []
    for i in range(1, abs(n) + 1 ):
        if n % i == 0 :
            uoc.append(i)
            uoc.append(-i)
    return sorted(uoc)