def solution(n, k):
    drink = k-int(n/10)
    answer = 12000*n + 2000*drink
    return answer