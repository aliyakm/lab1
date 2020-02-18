n = int(input())
i = 2
for i in range(2, n+1):
    if n%i==0:
        print(i)
        exit(0)
    else:
        i=i+1