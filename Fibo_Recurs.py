"Program for Fibonacci Series Using Recurssion"

def fiboSeries(i):
    if i <= 1:
        return i
    else:
        return (fiboSeries(i - 1) + (fiboSeries(i - 2))

num = int(input("Enter any Number: "))

if num <= 0:
    print("Number is negative")
else:
    print("Fibonacci series",end = " ")
for i in range(num):
    print(fiboSeries(i), end="")
