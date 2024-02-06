class A:
    def __repr__(self):
        return "42"

class B:
    def __repr__(self):
        return "42"


a = A()
b = B()
print(str(a))
print(repr(b))
print(str(b))

