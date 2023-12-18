num2=int(input("Enter a number:"))
num3=num2
ast=0
while num2!=0:
    rem=num2%10
    ast=ast+rem**3
    num2=num2//10
if ast==num3:
    print(ast,"is a amstrong number")
else:
    print(ast,"is not a amstrong number")