import sys

def main():
    n, k_val = map(int, input().split())
    a_list = list(map(int, input().split()))
    
    b = [0] * (n+1)
    for i in range(1, n+1):
        b[i] = a_list[i-1]
    
    F = [[-10**18] * (n+1) for _ in range(n+1)]

    for s in range(1, n+1):
        dp_seg = [-10**18] * (n+1)
        dp_seg[s] = b[s]
        if s < n:
            dp_seg[s+1] = b[s] + b[s+1]
        for i in range(s+2, n+1):
            dp_seg[i] = max(dp_seg[i-1], dp_seg[i-2]) + b[i]
        for i in range(s, n+1):
            F[s][i] = dp_seg[i] 
    dp2 = [[-10**18] * (n+1) for _ in range(k_val+1)]
    for j in range(0, k_val+1):
        dp2[j][0] = 0     
    for i in range(1, n+1):
        dp2[0][i] = F[1][i]
    if k_val >= 1:
        for j in range(1, k_val+1):
            prefix_max = [-10**18] * (n+1)
            current_max = -10**18
            for p in range(0, n+1):
                if dp2[j-1][p] > current_max:
                    current_max = dp2[j-1][p]
                prefix_max[p] = current_max
            
            for i in range(1, n+1):
                best_val = -10**18
                for s in range(1, i+1):
                    candidate = prefix_max[s-1] + F[s][i]
                    if candidate > best_val:
                        best_val = candidate
                dp2[j][i] = best_val   
    ans = -10**18
    for j in range(0, k_val+1):
        if dp2[j][n] > ans:
            ans = dp2[j][n]           
    print(ans)
if __name__ == '__main__':
    main()