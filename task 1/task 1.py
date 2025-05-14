s = str(input())
for c in s:
    cur = s.replace(c, '')
    rev_cur = cur[::-1]
    
    if cur == rev_cur:
        print("YES") 
        exit()

print("NO")
