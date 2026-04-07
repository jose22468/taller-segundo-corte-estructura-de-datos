n = int(input().strip())
s = input().strip()

ok = True

for i in range(n):
    if s[i] == '1':
        if i > 0 and s[i - 1] == '1':
            ok = False
            break
    else:
        left = (i > 0 and s[i - 1] == '1')
        right = (i < n - 1 and s[i + 1] == '1')
        if not left and not right:
            ok = False
            break

print("Yes" if ok else "No")