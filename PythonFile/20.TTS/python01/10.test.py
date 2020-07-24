def fibs(n):
    if n == 0 or n == 1:
        return 1
    else :
        return fibs(n-1) + fibs(n-2)
print(fibs(4))