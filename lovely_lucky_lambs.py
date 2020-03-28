def solution(total_lambs):
    return stingy_lamb(total_lambs) - generous_lamb(total_lambs)

def generous_lamb(total_lambs):  
    result = [1]
    total_lambs = total_lambs - result[0]
    while total_lambs >= 2*result[-1]:
        share = result[-1]*2
        result.append(share)
        total_lambs = total_lambs - share
    return len(result)
    # return result
    
def stingy_lamb(total_lambs):
    result = [1]
    total_lambs = total_lambs - result[0]
    while total_lambs >= sum(result[-2:]):
        if len(result) == 1:
            result.append(1)
            total_lambs = total_lambs - 1
        else:
            share = result[-1]+result[-2]
            result.append(share)
            total_lambs = total_lambs - share
    return len(result)
    # return result

if __name__ == "__main__":
    s = int(input())
    # print(solution(s))
    print(generous_lamb(s))
    print(stingy_lamb(s))