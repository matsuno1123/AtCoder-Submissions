"""
https://atcoder.jp/contests/abc409/tasks/abc409_c
"""

N, L = map(int, input().split())
D = list(map(int, input().split()))
D.insert(0, 0)

if L%3 != 0:
    print(0)
else:
    d_dict = {}
    now_d = 0
    for d in D:
        now_d = now_d+d if now_d+d<L else now_d+d-L
    
        if now_d in d_dict:
            d_dict[now_d] += 1
        else:
            d_dict[now_d] = 1
    
    distance = L//3
    
    result = 0
    
    for k, v in d_dict.items():
        if k >= distance:
            continue
    
        k2 = k+distance if k+distance < L else k+distance-L
        k3 = k2+distance if k2+distance < L else k2+distance-L
    
        if k2 in d_dict and k3 in d_dict:
            result += d_dict[k] * d_dict[k2] * d_dict[k3]
    
    print(result)