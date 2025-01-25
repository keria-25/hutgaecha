def solution(n):
    answer = 0
    for k in range(0,n+1):
        if k % 2 == 0:
            answer += k
    return answer