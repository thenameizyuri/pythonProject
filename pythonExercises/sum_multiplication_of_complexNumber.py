# (a+bi)(c+di) = (ac-bd)+(ad+bc)i

class Complex:
    def __init__(self, r , i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):
        return Complex(self.real + other.real , self.imaginary + other.imaginary)

    def __mul__(self, other):
        mulReal = self.real * other.real - self.imaginary * other.imaginary
        mulImag = self.real * other.imaginary + self.imaginary * other.real

        return Complex(mulReal , mulImag)

    def __str__(self):
            return f'{self.real}+{self.imaginary}i'


realpart = int(input("Enter the real part of 1st complex number\n"))
realImag = int(input("Enter the imaginary part of 1st complex number\n"))
real2part = int(input("Enter the real part of 2nd complex number\n"))
real2Imag= int(input("Enter the imaginary part of 2nd complex number\n"))

c1 = Complex(realpart , realImag)
c2 = Complex(real2part, real2Imag)

print(c1+c2)
print(c1*c2)

