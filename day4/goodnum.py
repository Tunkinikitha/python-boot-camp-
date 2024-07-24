#good numbers
import math
arr=[35,9,1,65,126,133]
count=0
for ele in arr:
    low=1
    high=math.ceil(ele**0.3)
    while low<high:
        res=low**3 + high**3
        if res==ele:
            count+=1
        if res<ele:
            low+=1
        else:
            high-=1
print('the count is:',count)
