def gcd(p,q):
    if q == 0:
        return p
    else:
        r = p % q
        return gcd(q,r)
if __name__ == '__main__':
    print(gcd(10,100))
