n=int(input())
run=True 
while run:
    if n%2!=0 and n>2:
        print("NO")
        run=False
    elif n%2==0:
        n=n/2
    elif n==1:
        print("YES")
        run=False