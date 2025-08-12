def f(x):
    a=float(x)
    b=int(x)
    c=a-b
    if c>=0.69:
        print (b,'+')
    else:
        print (b)

x=float(input('input a number: '))
while x>0:
    f(x)
    x=float(input('input a number: '))


