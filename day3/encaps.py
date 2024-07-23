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
