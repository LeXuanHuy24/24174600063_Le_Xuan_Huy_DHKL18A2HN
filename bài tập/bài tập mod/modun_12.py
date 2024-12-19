def ham_tich_cua_danh_so(*tham_so):
    tich = 1 
    for bo in tham_so :
        tich *= bo
    return tich 