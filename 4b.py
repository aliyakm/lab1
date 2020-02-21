A=int(input())
B=int(input())
if A<B:
    for x in range(A, B+1):
        print(x)
elif A>=B: 
    for i in range(A, B-1, -1):
        print(i)
