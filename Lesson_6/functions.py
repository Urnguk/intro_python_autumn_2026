# def func():
#     print("Hello World")
#     return True
#
# def sum_func(x, y):
#     return x + y
#
# z = sum_func(0, 1)
# print(z)
# print(sum_func(1, 2))
# print(func())

# def f(x):
#     print(1)
#     res = g(x)
#     print(1)
#     return res
#
# def g(x):
#     print(2)
#     res = z(x)
#     print(2)
#     return res
#
# def z(x):
#     print(3)
#     res = x
#     print(3)
#     return res
#
# print(f(True))


# value / a = b => value = a * b

def prime(value):
    if value < 2:
        return False
    div = 2
    while div ** 2 <= value:
        if value % div == 0:
            return False
        div += 1
    return True
#
#
# for i in range(1000):
#     if prime(i):
#         print(i)


# print(prime, type(prime), type(0))

# x = prime
# print(x(7))
#
# def f(x):
#     return x ** 2
# f = lambda x: x ** 2


# A = [333, 2, 8, 0, 4, -46, 7, 12, 33, 70, 10, 0]
# A.sort(key=lambda x: len(str(x)))
# print(A)

def second_element(value):
    return value[1]

A = [[2, 3], [4, 5], [7, 0], [3, 3], [6, 2], [6, 0]]
A.sort(key = lambda x: x[0])
print(A)

A = [[2, 3], [4, 5], [7, 0], [3, 3], [6, 2], [6, 0]]
A.sort(key=second_element)
A.sort(key = lambda x: x[0])
print(A)




