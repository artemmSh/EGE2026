with open('../files/26_4604.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes.sort(reverse=True)

used_boxes = [boxes[0]]
for box in boxes[1:]:
    if used_boxes[-1] - box >= 3:
        used_boxes.append(box)

used_boxes = used_boxes[:-1]
for box in boxes:
    if used_boxes[-1] - box >= 3:
        used_boxes.append(box)
        break

print(len(used_boxes), used_boxes[-1])
