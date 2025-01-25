def solution(n):
    answer = 0
    for k in range (1,n+1):
        if k ** 2 == n:
            answer = 1
            break
        else:
            answer = 2
    return answer