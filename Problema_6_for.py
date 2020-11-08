n=int(input("Introduceti un nr "))
s1=0
s2=0
s4=0
s5=0
s6=0
s3=0
fact=1
for n in range (1,n+1):
    s1=s1+n
for n in range (1,n+1):
    s2+=(n-1)*n
for n in range (1,n+1):
    fact= fact * n
    s3=s3+fact
for n in range (1,n+1):
    s4+=(2*n)+10
for n in range (1,n+1):
    s5+=n/(n+1)
for n in range (1,n+1):
    s6+=2*n
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

