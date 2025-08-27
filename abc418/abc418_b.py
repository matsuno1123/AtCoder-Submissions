"""
https://atcoder.jp/contests/abc418/tasks/abc418_b
"""

S = input()
result = 0
for i in range(len(S)-1):
    for j in range(i+1, len(S)):
        if S[i] != "t" or S[j] != "t" or j+1-i < 3:
            continue
        count = S[i:j+1].count("t")
        per = (count-2)/(j-i-1)
        if result < per:
            result = per

print(result)