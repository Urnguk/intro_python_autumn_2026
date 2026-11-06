# class Student:
#     def __init__(self, name="Egor", age=18, group=606, money=0):
#         self.name = name
#         self.age = age
#         self.group = group
#         self.money = money
#
#
#     def get_scholarship(self, amount=7700):
#         self.money += amount
#
#
# A = Student(name="Arthur", money=2000)
# B = Student()
#
#
# print(A.name, A.age)
# print(B.name, B.age)
# B.get_scholarship()
# print(A.money, B.money)


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)


X = Vector3D(1, 2, 3)
Y = Vector3D(4, 5, 6)
print(abs(X))
print(X + Y)







