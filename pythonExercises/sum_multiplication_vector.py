class Vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        str1 =''
        index = 0
        for i in self.vec:
            str1+= f'{i}a{index}+'
            index+=1
        return str1[:-1]
    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+vec2.vec[i])
        return Vector(newList)
    def __mul__(self, vec2):
        mul = 0
        for i in range(len(self.vec)):
            mul+= self.vec[i]*vec2.vec[i]
        return mul
    def __len__(self):
        return len(self.vec)


v1 = Vector([2,3,4])
v2 = Vector([4,5,3])
print(v1+v2)
print(v1*v2)
print(len(v1))
print(len(v2))