with open('files/26_4712.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes.sort(reverse=True)

current_box = boxes[0]
cnt = 1

for box in boxes:
    if current_box - box >= 3:
        cnt += 1
        current_box = box
print(cnt, current_box)
