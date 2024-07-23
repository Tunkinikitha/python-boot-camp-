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