def kiem_tra_so_nguyen_to(x):
    if x < 2:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True 