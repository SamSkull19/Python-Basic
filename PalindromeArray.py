# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G

n = int(input())
a = list(map(int, input().split()))
b = a[::-1]

if a == b:
    print("YES")
else:
    print("NO")