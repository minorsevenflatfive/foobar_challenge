def solution(l):
    lucky_triple = 0
    
    counter = [0]*len(l)
    for i in range(len(l)):
        for j in range(i):
            if(l[i] % l[j] == 0):
                counter[i] += 1
                lucky_triple += counter[j]
        
    return lucky_triple

if __name__ == "__main__":
    print(solution(list([1,2,3,4,5,6,7,8])))
    for i in range(1):
        print(i)