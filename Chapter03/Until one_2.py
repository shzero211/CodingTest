n,k=map(int,input().split())
result=0

while True:
    #(n==k 로 나누어 떨어지는 수)가 될때까지 1씩 빼기
    target=(n//k)*k
    result+=(n-target)
    n=target
    #n이 k보다 작을때 반복문탈출
    if n<k:
        break
    result+=1
    n//=k

result+=(n-1)
print(result)