n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

new_scores = [(s / max_score) * 100 for s in scores]

print(sum(new_scores) / n)