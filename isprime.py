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
