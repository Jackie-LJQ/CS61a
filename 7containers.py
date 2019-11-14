def find_element(s, value):
    """search element in s"""
    amount = 0
    for element in s:
        if element == value:
            amount += 1
    return amount
s = [1, 3, 5, 7, 9, 1]
num_1 = find_element(s, 1)

pair = [[1, 2], [3, 4], [9,10], [7, 7], [4, 5]]
for x, y in pair:
    if x == y:
        f = 1

list(range(1, 5))
"""range: consecutive integers, use list get [1, 2, 3, 4]"""

def cheer():
    """ _ means we don't concern the name, just do fixed number of time"""
    for _ in range(3):
        print('fight on Trojan')

def divisor(n):
    return [1] + [x for x in range(2, n) if n % x == 0] + [10]

c = "strings"
T = "ing" in c
R = c[3]
"""T is True, R is "r" """
