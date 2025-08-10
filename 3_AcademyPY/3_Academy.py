def main():
    N = int(input().strip())
    S = input().strip()
    
    A = [0]
    
    for i in range(1, N + 1):
        pos = A.index(i - 1)
        
        if S[i-1] == 'L':
            A.insert(pos, i)
        else:
            A.insert(pos + 1, i)
    
    print(" ".join(map(str, A)))

if __name__ == "__main__":
    main()