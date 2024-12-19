def kiem_tra_so_chinh_phuong(n):
    if n < 0:
        return False
    can = int(n**1/2)
    return can*can == n