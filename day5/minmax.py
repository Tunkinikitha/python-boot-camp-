#n1=7823,n2=5489,n3=1384
#sum of all min digit 
#sum of all max digit ,and find the difference
n1=7823
n2=5489
n3=1384
min_sum=[]
max_sum=[]
def min_check(n):
    s=str(n)
    min=int(s[0])
    for i in s:
        if int(i)<min:
            min=int(i)
    return min
def max_check(n):
        s=str(n)
        max=int(s[0])
        for i in s:
            if int(i)>max:
                max=int(i)
        return max    
min_sum=min_check(n1)+min_check(n2)+min_check(n3)
max_sum=max_check(n1)+max_check(n2)+max_check(n3)
diff=abs(min_sum-max_sum)
print(diff)
