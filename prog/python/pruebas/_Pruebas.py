def fun(x, y=[]):
    y.append(x)
    return y
print(fun(1))
print(fun(2))
print(fun(3, []))
print(fun(4))