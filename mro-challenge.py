class A:
    def hello(self):
        print('Hello from A!')

class B(A):
    pass

class C:
    def hello(self):
        print('Hello from C!')

class D(B):
    pass

class E(C):
    def hello(self):
        print('Hello from E!')

class F(E, D):
    pass

f = F()
f.hello()