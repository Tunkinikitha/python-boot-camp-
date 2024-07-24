#n=101011 binary to decimal(32+8+2+1=43)
n=101011
sum=0
i=0
while n>0:
     rem=n%10
     pro=rem*pow(2,i)
     sum+=pro
     i+=1
     n=n//10
print(sum)