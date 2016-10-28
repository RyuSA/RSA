#coding:utf-8
import random

def is_prime(n):
    # Miller–Rabin primality test
    # if p is even or minus, return False
    # we don't need 2
    if not n&1 or n < 0:
        return False

    # n = 2^s * d + 1
    s = 1
    d = (n-1) >> 1
    while not d&1:
        # d is divided by 2
        d = d >> 1
        # upgrade s
        s += 1

    # this number is related to sucsess probability
    times = 20

    for i in xrange(times):
        # flag will be used for line 40
        flag = True
        # b is a base
        b = random.randint(2,n-1)
        # X = b^d mod n
        X = pow(b,d,n)

        # if X is 1 or -1, then this 'b' pass the test. go next b
        if X == 1 or X == n-1:
            continue

        for j in xrange(s):
            X = pow(X,2,n)
            # X = b^(2r)d mod n
            if X == n-1:
                # pass the test, go next b
                flag = False
                break
        if flag:
            # flag has not been modifyied, which mean we never obtain -1
            return False

    # pass times times text, this n may be prime number
    return True

def generate_primes(k):
    # if k is small, it is not good for RSA
    if k < 5:
        return False
    # generate k bit 2 safe primes
    k -= 3
    # to create safe prime
    minimum = 1 << k
    maximum = (1 << k+1) -1

    while True:
        prime1 = generate_prime(minimum,maximum)
        prime2 = generate_prime(minimum,maximum)
        # if you are really lucky, try again
        if prime1 != prime2:
            return (prime1,prime2)

def generate_prime(m,M):
    while True:
        prime = random.randint(m,M)
        # let prime be odd number
        prime = (prime << 1) + 1
        # prime is prime number ?
        if is_prime(prime):
            prime = (prime << 1) + 1
            # prime is a safe prime?
            if is_prime(prime):
                return prime

def gcd(a,b):
    while b :
        a , b = b , a%b
    return a

def lcm(a,b):
    return a*b / gcd(a,b)

def prime_lcm(p,q):
    """Be careful. p, q are prime to use this function"""
    return (p-1)*(q-1)

def extendEuclid(a,b):
    flag = False
    if a < b:
        a ,b = b, a
        flag = True
    """find the integers x,y such that xa + yb = 1"""
    if b == 0:
        x = 1
        y = 0
    else :
        # e = 1 << 16 +1
        q = a/b
        r = a%b
        (u,v) = extendEuclid(b,r)
        x = v
        y = u - q*v
    if flag:
        return (y,x)
    return (x,y)

# print extendEuclid(13,5)
