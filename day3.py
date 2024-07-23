#class,obj,constructor,encap,inher,poly,abst
#object contain properties,behaviour(fun),identity(unique) ,object is a real world entity ,object is an instance(copy or sub part) of a class
#class is a logical entity ,class contains fun,constructors,data ,class is a blue print of an object
#constructor is a special method which is used to invoke instance variable,const does not return any value,while creating the object constructor will call implict(default,calling itself)
#3 types of const default,parameterised,non parameterised
#string->8bytes,int->4bytes
class student:
    def __init__(self,name,roll,branch,add,email):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.add=add
        self.email=email
    def display(self):
        print('name is:',self.name)
        print('roll is:',self.roll)
        print('branch is:',self.branch)
        print('add is:',self.add)
        print('email is:',self.email)
s1=student('nikitha','5j8','cse','mbnr','nikki@gmail.com')
s1.display()
#8+4+8+8+8=36*240=8640

#static->used for memory management,used to reduce the space,instead of creating individually a common data create a static data and pass the copy to all the objects
class student:
    branch='cse'#static data
    def __init__(self,name,roll,add,email):#const
        self.name=name
        self.roll=roll
        self.add=add
        self.email=email
    def display(self):
        print('name is:',self.name)
        print('roll is:',self.roll)
        print('branch is:',student.branch)
        print('add is:',self.add)
        print('email is:',self.email)
        print()#space
s1=student('nikitha','5j8','mbnr','nikki@gmail.com')
s2=student('bhavana','5j1','tdr','bhav@gmail.com')
s1.display()
s2.display()
#8+4+8+8=28*240=6720

#without display fun ,using str 
class student:
    branch='cse'#static data
    def __init__(self,name,roll,add,email):#const
        self.name=name
        self.roll=roll
        self.add=add
        self.email=email
    def __str__(self):
        return f'{self.name} {self.roll} {student.branch} {self.add} {self.email}'
s1=student('nikitha','5j8','mbnr','nikki@gmail.com')
s2=student('bhavana','5j1','tdr','bhav@gmail.com')
print(s1)
print(s2)

#abstraction ->hidding  the data
#inheritence->inheriting the data from base class(parent)to the derived class(child),single,multiple,multilevel,hybid,hierarical
class jntuh:
    def schedule_acacdemics():
        print("scheduling acadamics")
    def declare_holidays():
        print('national and summar holidays')
    def result():
        print('go to www.jntuhresult.com')
class sridevi(jntuh):
    def fees():
        print('3rd yr fee is 85k')
sobj=sridevi        
sobj.fees()
sobj.schedule_acacdemics()
sobj.declare_holidays()
sobj.result()


class rbibank():
    def interest():
        pass
    def loan():
        print('provide home loans')
class hdfc(rbibank):
    def interest():
        print('7.5% interrest')
class sbi(rbibank):
    def interrest():
        print('11% interest')
aobj=rbibank
aobj.interest()
aobj.loan()

class jntuh:
    def schedule_acacdemics():
        print("scheduling acadamics")
    def declare_holidays():
        print('national and summar holidays')
    def result():
        print('go to www.jntuhresult.com')
class sridevi(jntuh):
    def fees():
        print('3rd yr fee is 85k')
sobj=sridevi
sobj.fees()
sobj.schedule_acacdemics()
sobj.declare_holidays()
sobj.result()

from abc import ABC
class vehicle(ABC):
    def speed():
        pass
    def milage():
        pass
    def model():
        pass
    def brreak():
        print('stop the vehicle')
class rangerover(vehicle):
    def speed():
        print('450 max speed')
    def milage():
        print('12kmph')
    def model():
        print('jgkggkk')
class fortune(vehicle):
    def speed():
        print('300 max speed')
    def milage():
        print('11kmph')
    def model():
        print('jgkggkr')
fobj=rangerover
fobj.speed()
fobj.milage()
fobj.brreak()
fobj.model()   

#encapsulation->binding data and methods into the single component 
#ex:class is the best example of encapsulate,adv:code integration,security,acess modifiers:public,private,protected
class employee:
    def __init__(self):
        self.name='nikitha'
        self.role='developer'
        self.__salary='90000'
    def get_salary(self):
        return self._salary
    def display(self):
        print(self.name,self.role)
e1=employee()
e1.display()

class employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def empdisplay(self):
        print(self.name,self.role)
class company(employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):
        print('hiring for the manager role')
cobj=company('wipro','gachibowli')
eobj=employee('nikitha','dev',90000)
eobj.empdisplay()
print(cobj._hiring())

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

    

    



    




    
