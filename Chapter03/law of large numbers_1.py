#첫번째 풀이
n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
#첫번째로 큰값
first=data[n-1]
#두번쨰로 큰값
second=data[n-2]

result=0

while True:
    for i in range(k):
        if m==0:
            break
        result+=first
        m-=1

    if m==0:
        break
    result+=second
    m-=1

print(result)
