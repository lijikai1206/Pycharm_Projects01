def make_power(x):
    def fn(arg):
        return arg ** x
    return fn

f2 = make_power(2)
y = f2(100)
print(y)