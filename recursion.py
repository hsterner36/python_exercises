def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print("Test af fib", fib(12))

def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)

print("Test af sum", sum(10))


def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print("Test af fac",fac(7))