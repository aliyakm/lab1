a=float(input())
b=a%1
b1=int(120*b)

c=a%10-b
c1=int(2*c)

d=a%100-b-c
d1=int(d/30)
print(d1, c1, b1)