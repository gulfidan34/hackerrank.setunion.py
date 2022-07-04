# Enter your code here. Read input from STDIN. Print output to STDOUT
n =int(input())
x= list(input().split())
b =int(input())
y= list(input().split())

s1 = set(x)
s2 = set(y)
print(len(s1.union(s2)))
