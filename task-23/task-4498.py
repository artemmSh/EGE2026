def f(start, end, res=''):
    if start > end or res.count('1') > 4 or res.count('3') > 5: return 0
    if start >= end and res.count('1') <= 4 and res.count('2') >= 2 and res.count('3') == 5: return start == end
    return f(start * 5, end, res + '1') + f(start * 3, end, res + '2') + f(start + 45, end, res + '3')


print(f(1, 2970))
