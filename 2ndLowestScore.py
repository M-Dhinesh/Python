lst1=[]
lst2=[]
name=[]
a=int(input())
for i in range(a):
    c=input()
    lst1.append(c)
    b=input()
    lst2.append(b)
z=min([eval(i) for i in lst2])
z=str(z)
for i in lst2:
    if i==z:
        y=lst2.index(i)
        lst1.pop(y)
        lst2.pop(y)
x=min([eval(i) for i in lst2])
x=str(x)
for i in range(len(lst2)):
    if lst2[i]==x: 
       print(lst1,x)
       name.append(lst1[i])
m=sorted(name)  
for i in m:
    print(i)