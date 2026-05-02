with open('files/26_20815.txt') as file:
    N, K = map(int, file.readline().split())
    astronauts = list()
    for i in file:
        astronaut_id, score, interview = list(map(int, i.split()))[0], sum(list(map(int, i.split()))[1:]), list(map(int, i.split()))[-1]
        astronauts.append([astronaut_id, score, interview])

astronauts.sort(key=lambda x: (-x[1], -x[2], x[0]))
accepted = astronauts[:K]
rejected = astronauts[K:]

if accepted[-1][1] != rejected[0][1]:
    passed_score = accepted[-1]
else:
    half_passed_score = accepted[-1]
    passed_score = [astr[0] for astr in astronauts if astr[1] > half_passed_score[1]][-1]

cnt = sum(astr[1] == half_passed_score[1] for astr in astronauts)
print(passed_score, cnt)
