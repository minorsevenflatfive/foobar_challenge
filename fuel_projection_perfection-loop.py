def solution(n):
    queue = []
    visited=[]
    n = int(n)
    step = 0
    if n == 1:
        return step
    queue.append(n)
    while True:
        qlength = len(queue)
        # print('q'+str(queue))
        # print('v'+str(visited))
        while qlength > 0:
            temp_n = queue.pop(0)
            if temp_n == 1:
                return step
            if temp_n not in visited:
                if temp_n%2 == 0:
                    queue.append(temp_n//2)
                else:
                    queue.append(temp_n+1)
                    queue.append(temp_n-1)
            qlength -= 1
            visited.append(temp_n)
        step += 1

if __name__ == "__main__":
    n = input()
    print(solution(n))
