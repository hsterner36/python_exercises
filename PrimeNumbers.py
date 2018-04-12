# Some very naive prime number methods for a basic course in Python
# Copyright (C) HST

#check if n is prime
def isPrime(n):
    if n == 2: return True
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
#returns a list of the  primefactorization of a natural number
def primeFactorize(n):
    primes = []
    if n==2: return [2]
    for i in range(2,n):
        if n % i == 0 and isPrime(i):
            while (n%i==0):                
                primes.append(i)
                n=n/i
    return primes


#generate primes from 2..n
def genPrimes(start,end):
    for i in range(start,end):
        if isPrime(i):
            listofprimes.append(i)
    return listofprimes

#generate the first n primes:
def genNPrimes(N):
    listofprimes = []
    i = 0 #number of primes
    k=2 #iterating prime suspect
    while i<N:
        if isPrime(k):
            listofprimes.append(k)
            i=i+1
        k = k + 1
    return listofprimes

#save from 2 to n primes to  file
def savePrimes(n,filename):
    file = open(filename,"w")
    listofprimes = genPrimes(2,200)
    for i in listofprimes:
        file.write(str(i)+ "\n")
    file.close() 
    print("Wrote from %d prime numbers to the file %s" % (n,filename))

if __name__ == "__main__":
    print(primeFactorize(18))
