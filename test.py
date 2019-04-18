a = [0, 1]
for i in range(1, 11):
    a.append(a[-1] * 10 + 5 * (10 ** (i - 1)))
print(a)
ans = 0
s = "866278171"
l = len(s)
for i in range(len(s)):
    if int(s[i]) > 3:
        ans = ans + int(s[i]) * a[l - 1 - i] + 10 ** (l - 1 - i) // 2
    else:
        ans = ans + int(s[i]) * a[l - 1 - i]
print(ans)
