n=int(input())
a=float(input())
s=sum([(a**i) for i in range(1, n+1)])
print(s+1)
