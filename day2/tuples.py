#tuples
#collection of mul data ele immutable
student=(101,'umer','cse','hyd')
#student.append('sridevi')#attributre error
print(student)

student=(101,'umer','cse','hyd')
student=list(student)
student[2]='ece'
print(student)
