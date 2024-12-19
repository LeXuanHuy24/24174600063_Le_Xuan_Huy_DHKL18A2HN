def bien_doi_so_thap_phan(n):
    chuyen = str(n)
    if '.' in chuyen:
        phan_thap_phan = len(chuyen.split('.')[1])
        mau_so = 10 ** phan_thap_phan
        tu_so = round(n * mau_so) 
    else:
        tu_so = int(n)
        mau_so = 1
    def tim_ucln(a, b):
        
        while b != 0:
            a, b = b, a % b
        return a
    ucln = tim_ucln(tu_so, mau_so)
    tu_so //= ucln
    mau_so //= ucln

    return tu_so, mau_so