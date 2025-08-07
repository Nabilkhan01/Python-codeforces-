n = int(input())
count =0
for i in range(n):
    P,V,T=list(map(int,input().split()))
    if P+V+T >= 2:
        count+=1
print(count)