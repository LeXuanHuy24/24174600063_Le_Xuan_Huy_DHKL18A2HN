def uclln(a, b):
    if b == 0:  
        return abs(a)
    return uclln(b, a % b) 