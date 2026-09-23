drinks=int(input())
proportions=map(float,input().split())
w=sum(proportions)
result=w / drinks
print(result)