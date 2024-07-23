#polymorphism->
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name} {self.age}'
class student(person):
    def __init__(self,name,age,roll,branch):
        super().__init__(name,age)
        self.roll=roll
        self.branch=branch
    def __str__(self):
        perdetails=super().__str__()
        return f'{perdetails},{self.roll},{self.branch}'
class anualday(student):
    def __init__(self, name, age, roll, branch,program):
        super().__init__(name, age, roll, branch)
        self.program=program
        def __str__(self):
            studetails=super().__str__()
            return f'{studetails},{self.program}'
aobj=anualday('nikitha',20,'j8','cse','solo')
print(aobj)
        
s=input()
ucount,lcount,dcount,scount=0,0,0,0
for c in s:
    if c.isupper():
        ucount+=1
    elif c.islower():
        lcount+=1
    elif c.isdigit():
        dcount+=1
    else:
        scount+=1
if len(s)>8 and ucount>0 and lcount>0 and dcount>0 and scount>0:
    print('valid')
else:
    print('invalid')
