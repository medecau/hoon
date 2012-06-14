class Fibonacci(object):
    a, o=0, 1
    def __init__(self):
        pass
    def next(self):
        self.a, self.o = self.o, self.a+self.o
        return self.o

def fibseq(num):
    '''
        Returns the fibonacci sequence in a list up to num
    '''
    seq=[]
    f=Fibonacci()
    for i in range(num):
        seq.append(f.next())
    return seq

def isprime(num):
    '''
        Checks for the primality of a number
    '''
    from math import ceil
    from math import sqrt
    if (num%2 == 0 and num>2) or num < 2 or type(num) is not int:
        return False
    else:
        l=int(ceil(sqrt(num)))
        for i in xrange(3, l+1, 2):
            if num%i==0:
                return False
        return True

def nextprime(num):
    '''
        Returns the next prime
    '''
    if num > 2:
        if num%2==0:
            num-=1
        else:
            pass
        while True:
            num+=2
            if is_prime(num):
                return num
            else:
                continue
    elif num == 2:
        return 3
    else:
        return 2

def factor(num, short=False):
    '''
        Calculates the factors of num
        TODO: remove short
    '''
    from math import ceil
    from math import sqrt
    factors=[]
    square=sqrt(num)
    if square == int(square):
        factors.append(int(square))
    for f in xrange(1,int(ceil(square))):
        if num%f==0:
            factors.extend([f, int(num/f)])
    if short:
        factors.sort()
        return factors[1:-1]
    else:
        return factors