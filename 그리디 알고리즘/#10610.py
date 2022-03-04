num=list(input())
num.sort(reverse=True)

a=0

for i in num:
    a+=int(i)

if a%3==0 and '0' in num:
    print(''.join(num))
else:
    print(-1)
