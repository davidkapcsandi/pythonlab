#Task
#Create a Student class that takes the name and age on creation.
#Create 2 objects of your student class and get the age of one of them.
class Student:
    def __init__(self, name, age, class_ = "Student"):
        self.name = name
        self.age = age
        self.class_ = class_
        
    def average(self, score1, score2, score3):
        x = (score1 + score2 + score3) / 300*100
        return f"{self.name} - average test score is {x}%"
    
student = Student("person", 5)

print(student.average(20,60,60))

class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan
    
    def fly(self):
        print(f"{self.name} is flyting with a winspan of {self.wingspan} cm")
    
    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"
class Owl(Bird):
    def __init__(self, name, wingspan, nocturnal = True):
        super(). __init__(name, wingspan)
        self.nocturnal = nocturnal
    def goot(self):
        print(f"{self.name} is hooting")

    def __str__(self):
        return super().__str__() + f" - nocturnal: {self.nocturnal}"
class Dodo(Bird):
    def __init__(self,name,wingspan, extinct = True):
        super().__init__(name, wingspan)
        self.extinct = extinct
    def __str__(self):
        return super().__str__() + f"- extinct: {self.extinct}"
bird1 = Bird("eagle",  20)
owl1 = Owl("barn owl", 90 )
dodo1 = Dodo("whatever", 100)

bird1.fly()
print(bird1)

owl1.fly()
print(owl1)

dodo1.fly()
print(dodo1)