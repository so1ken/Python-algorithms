def count_ap_subarrays(array):
    n = len(array)
    ans = 0

    for l in range(n):
        for r in range(l + 2, n):
            found = False
            for i in range(l, r - 1):
                for j in range(i + 1, r):
                    for k in range(j + 1, r + 1):
                        if array[j] * 2 == array[i] + array[k]:
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                ans += n - r
                break
    return ans

n = int(input())
array = [int(num) for num in input().split()]

print(count_ap_subarrays(array))
