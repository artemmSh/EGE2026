with open('files/26_12113.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes.sort(reverse=True)
start_even = max(i for i in boxes if i % 2 == 0)
start_odd = max(i for i in boxes if i % 2)


def result(start, unit):
    current_box = start
    cnt = 1
    for box in boxes:
        if current_box - box >= unit and (current_box % 2) != (box % 2):
            cnt += 1
            current_box = box
    return cnt, current_box


answer = [result(start_even, 7), result(start_odd, 7)]
answer.sort(reverse=True)
print(*answer[0])
