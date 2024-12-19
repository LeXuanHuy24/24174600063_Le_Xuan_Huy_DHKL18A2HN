def kiem_tra_so_hoan_hao(n):
    tong=0 
    if n.isdigit() and int(n) > 0  :
        n = int(n)
        return True
        for i in range(1,n):
            if n % i == 0 :
                tong += i 
        return tong == n
    return False