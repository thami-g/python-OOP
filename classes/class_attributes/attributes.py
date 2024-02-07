class A:
    a = "I am a class attribute!"


x = A()
y = A()
print(x.a)
print(y.a)
x.a = "This creates a new instance attribute for x!"
print(y.a)
print(A.a)
A.a = "This is changing the class attribute 'a'!"
print(y.a)
print(x.a)
# Python's class attributes and object attributes are stored in separate dictionaries
print(x.__dict__)
print(y.__dict__)
print(A.__dict__)
print(x.__class__.__dict__)
