
https://atcoder.jp/contests/arc005/tasks/arc005_1
"""

input()
target = ["TAKAHASHIKUN", "Takahashikun", "takahashikun", "TAKAHASHIKUN.", "Takahashikun.", "takahashikun."]
print(len([word for word in input().split() if word in target]))