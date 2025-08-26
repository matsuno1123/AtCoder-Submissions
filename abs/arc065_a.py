
https://atcoder.jp/contests/abs/tasks/arc065_a
"""

S = input()

result = "NO"
while True:
    if S == "":
        result = "YES"
        break
    elif S.endswith("dream"):
        S = S[:-5]
    elif S.endswith("dreamer"):
        S = S[:-7]
    elif S.endswith("erase"):
        S = S[:-5]
    elif S.endswith("eraser"):
        S = S[:-6]
    else:
        break

print(result)