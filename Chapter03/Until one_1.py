#첫번째 풀이
n,k=map(int,input().split())
result=0
#k보다 크면 무조건 나눠주기위해서 뺄샘을 해주면서 나눠주기
while n>=k:

    while n%k != 0:
        n-=1
        result+=1
    n//=k
    result+=1
#나눠지지 않다면 마지막으로 1이될때까지 뺴줘야한다.
while n>1:
    n-=1
    result+=1

print(result)

