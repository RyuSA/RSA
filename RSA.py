#coding:utf-8
import integer as Int

def create_generater(k):
    """create k bit 2 safe primes"""
    return Int.generate_primes(k)

def create_public_key(primes):
    (p,q) = primes
    L = Int.prime_lcm(p,q)
    # k = max(len(bin(p)),len(bin(q)))
    key = (1 << 16) + 1
    while True:
        # print 'a'
        if Int.gcd(key,L) == 1:
            return key
        key += 2

def create_secret_key(primes,public):
    (p,q) = primes
    L = Int.prime_lcm(p,q)
    (d,dust) = Int.extendEuclid(public,L)
    if d < 0:
        d += L
    return d

def generate_keys(str,level):
    if not level:
        level = 100
    elif level == 1 :
        level = 1024
    elif level == 2 :
        level = 2048
    else :
        return False
    primes = create_generater(level)
    n = primes[0]*primes[1]
    del primes
    publickey = create_public_key(primes)
    secretkey = create_secret_key(primes,publickey)
    return (n,publickey,secretkey)

def encrypt(str,public):
    str = trans(str)
    (n,publickey) = public
    return pow(str,publickey,n)

def decrypt(str,public,private):
    return trans(pow(str,private,public[0]))
