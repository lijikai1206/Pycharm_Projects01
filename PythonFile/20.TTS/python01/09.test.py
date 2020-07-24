def div(x, y):
    if y == 0:
        raise ZeroDivisionError("y的值为0")
    else:
        return x / y
print(div(100,2))