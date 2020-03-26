def solution(x,y):
    prisoner_id = 1
    traverse_x = 2
    for _ in range(x-1):
        prisoner_id = prisoner_id + traverse_x
        traverse_x = traverse_x + 1
    for _ in range(y-1):
        prisoner_id = prisoner_id + x
        x = x + 1
    return prisoner_id

if __name__ == "__main__":
    inp = input().split()
    x,y = int(inp[0]),int(inp[1])
    print(solution(x,y))

    
