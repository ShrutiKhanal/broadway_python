#Hybrid

class A:
    a = 1


class B(A):
    a = 2


class C(A):
    a = 3


class D(B, C):
    pass

print(D.mro())
obj = D()
print(obj.a)