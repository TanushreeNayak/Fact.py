"A program For Factorial"


a = float(input("enter a :" ))
b = int(input("enter b : "))

#Formula
d = b*b-4*a*c

#conditions apply
if d< 0:
    print("no real roots.")
elif d == 0:
    r1=r2=-b
    print("real and equal roots",r1,r2)
else:
    r1 =(-b + d**0.5)/(2*a)
r2=(-b -d ** 0.5) / (2 * a)
print("real and unequal roots",r1,r2)
