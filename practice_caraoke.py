n, m = map(int, input().split())
answer = []
for _ in range(m):
    answer = int(input())

max_score = 0
for _ in range(n):
    score = 100
    for i in range(m):
        list = int(input())
        if answer[i] - list[i] <= 5:
            continue
        elif(answer[i] - list[i] <= 10):
            score -= 1
        elif(answer[i] - list[i] <= 20):
            score -= 2
        elif(answer[i] - list[i] <= 30):
            score -= 3
        else:
            score -= 5
    if max_score <= score:
        max_score = score

print(max_score)