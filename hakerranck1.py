n = int(input())
arr = input().split()
s = sorted(arr)
i = n
while i != 0:
    if s[i-1] != s[n-1]:
       print(s[i-1])
    break
i -= 1