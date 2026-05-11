with open(r'..\files\24_9753.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
l = 0
r = 0
while r < len(data):
    if cnt <= 150: r += 1
    else:
        ans = max(ans, r - l)
        l += 1
        if data[l] == 'Y': cnt -= 1

