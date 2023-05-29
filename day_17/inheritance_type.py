#Multiple inheritance

class A:
    a = 1


class B:
    a = 2


class C(A, B):
    pass


obj = C()
print(obj.a)


#Hierarchical inheritance

class A:
    a = 1


class B(A):
    a = 2


class C(A):
    a = 3


obj = C()
print(obj.a)


#Multi-level inheritance
#child bata khojdai jancha
class A:
    a = 1


class B(A):
    a = 2

class C(B):
    a = 3


class D(C):
    pass

obj = D()
(obj.a)


#Hybrid inheritance
class A:
    a = 1


class B:
    a= 2


class C(A, B): #multiple
    a= 3


class D(C):
    a = 4


class E(C):
    pass

print(E.mro()) #mro -> method resolution order #imp
