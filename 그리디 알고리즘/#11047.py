from audioop import reverse


N,K=map(int,input().split())
A=[]

for i in range(N):
    A.append(int(input()))
A.sort(reverse=True)
    
result=0
for i in A:
    if K==0:
        break
    result+=K//i
    K=K%i

print(result)
    
