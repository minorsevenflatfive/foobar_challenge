import re

def solution(s):
    possible_seq = []
    for i in range(1,len(s)+1):
        if len(s)%i == 0:
            ss = s[:i]
            if is_possible(ss, s):
                possible_seq.append(i)
    return len(s)//min(possible_seq)

def is_possible(ss, s):
    pattern = r"\b({})+\b".format(ss)
    matched = re.match(pattern, s)
    is_match = bool(matched)
    return is_match

if __name__ == "__main__":
    s = input()
    print(solution(s))

    
