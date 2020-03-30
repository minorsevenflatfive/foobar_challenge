def solution(n):
    n = int(n)
    step = 0
    if n == 1:
        return step
    while n != 1:
        if n%2 == 0:
            n = n//2
            step = step+1
        else:
            if isPowOf2(n-1):
                n = n-1
            elif isPowOf2(n+1):
                n = n+1
            else:
                n = n-1
            step = step+1
    return step

def isPowOf2(n):
    return (n & (n - 1)) == 0

if __name__ == "__main__":
    n = input()
    print(solution(n))
