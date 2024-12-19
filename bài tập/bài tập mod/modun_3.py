def kiem_tra_so_thuc(n):
    n = n.strip()
    if n.isdigit():
        return True
    if n.count('.') == 1:
        phan_truoc, phan_sau = n.split('.')
        return phan_truoc.isdigit() and phan_sau.isdigit()
    return False