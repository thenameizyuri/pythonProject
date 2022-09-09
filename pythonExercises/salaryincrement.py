class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sal):
        self.increment =  sal/self.salary

e = Employee()

#before
print(e.salaryAfterIncrement)
print(e.increment)

#after setter property
e.salaryAfterIncrement = 2000
print(e.increment)