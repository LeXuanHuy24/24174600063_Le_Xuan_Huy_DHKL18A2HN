import math 
def phan_so_toi_giam(tu, mau):
    if mau < 0 :
        tu = -tu 
        mau = -mau 
    ucln = math.gcd(tu,mau)
    tu_toi_gian = tu // ucln
    mau_toi_gian = mau // ucln
    return tu_toi_gian , mau_toi_gian