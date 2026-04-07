s = input().strip()

dp0 = dp1 = dp2 = 0

for ch in s:
    ndp0, ndp1, ndp2 = dp0, dp1, dp2

    if ch == 'a':
        ndp0 = dp0 + 1
        ndp2 = max(dp2 + 1, dp1 + 1)
    else:  # ch == 'b'
        ndp1 = max(dp1 + 1, dp0 + 1)

    dp0, dp1, dp2 = ndp0, ndp1, ndp2

print(max(dp0, dp1, dp2))