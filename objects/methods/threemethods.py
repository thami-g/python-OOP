class C:
    def m(self):
        print("C class")
    
x = C()
type(x).m(x)
C.m(x)
x.m()