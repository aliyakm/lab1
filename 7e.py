n=int(input())
run=True
i=0
while run:
    if 2**i>=n:
        print(i)
        run=False
    elif 2**i<n:
        i=i+1