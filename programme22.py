e=int(input())
list=list(map(int,input().split()))
ae=1
len=[]
for i in list:
  ae=ae*i
for i in list:
  len.append(ae//i)
print(*len)
