with open('files/26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    sailors = dict()
    for i in file:
        sailor_id, score, interview = list(map(int, i.split()))[0], sum(list(map(int, i.split()))[1:-1]), list(map(int, i.split()))[-1]
        sailors[sailor_id] = [score, interview]

sailors_copy = sailors.copy()
sailors = sorted(sailors, key=lambda x: (-sailors[x][0], -sailors[x][1], x))
sorted_sailors = dict()
for key in sailors:
    sorted_sailors[key] = sailors_copy[key]

last_passed = sailors[S - 1]
first_not_passed = sailors[S]
ans1 = 0

if sorted_sailors[last_passed][0] != sorted_sailors[first_not_passed][0]:
    ans1 = last_passed
else:
    half_passed_score = sorted_sailors[last_passed][0]
    ans1 = [key for key in sorted_sailors if sorted_sailors[key][0] > half_passed_score][-1]

ans2 = sum(sorted_sailors[key][0] == half_passed_score for key in sorted_sailors)
print(ans1, ans2)
