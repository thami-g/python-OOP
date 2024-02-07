class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


if __name__ == "__main__":
    x = C()
    print("Number of instances: : " + str(C.counter))
    y = C()
    print("Number of instances: :" + str(C.counter))
    del x
    print("Number of instances: :" + str(C.counter))
    del y
    print("Number of instances: :" + str(C.counter))
    
# Principially, we could have written C.counter instead of type(self).counter, because type(self)
# will be evaluated to "C" anyway. However we will understand later, that type(self) makes sense,
# if we use such a class as a superclass.
