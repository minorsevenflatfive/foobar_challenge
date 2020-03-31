def solution(n):
    map = {}
    n = int(n)
    return solutionHelper(n, map)

def solutionHelper(n, map):
    if n == 1:
        return 0
    if n in map:
        return map[n]
    if n%2 == 0:
        step = 1 + solutionHelper(n//2, map)
    else:
        alt1 = 1 + solutionHelper(n+1, map)
        alt2 = 1 + solutionHelper(n-1, map)
        step = min(alt1, alt2)
    map[n] = step
    return step

if __name__ == "__main__":
    n = input()
    print(solution(n))
