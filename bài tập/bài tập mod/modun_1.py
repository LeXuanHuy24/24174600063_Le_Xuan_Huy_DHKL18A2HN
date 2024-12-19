def kiem_tra_so_nguyen(n):
    n = n.strip()
    if not n :
        return False
    if n[0] in ('+','-'):
        return n[1:].isdigit()
    return n.isdigit()