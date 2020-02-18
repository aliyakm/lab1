a=int(input())
b=int(input())
c=int(input())
d=int(input())
def min4(a, b, c, d):
    a1=min(a, b)
    b1=min(c, d)
    c1=min(a1, b1)
    return c1
print(min4(a, b, c, d))