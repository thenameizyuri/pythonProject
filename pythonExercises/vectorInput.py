class C2dvec:
    def __init__(self, i , j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j'

class C3dvec(C2dvec): #inherit i,j from class C2dvec
    def __init__(self , i ,j, k):
        super().__init__(i,j)
        self.kcap = k
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j + {self.kcap}k'

icap = int(input("Enter the i variable "))
jcap = int(input("Enter the j variable "))
kcap = int(input("Enter the k variable "))
v2d = C2dvec(icap,jcap)
v3d = C3dvec(icap , jcap ,kcap)

print(v2d,'\n',v3d)