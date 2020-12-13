# linear_search.py
def linear_search(sequence, target):
    index = 0
    size = len(sequence)
    while index < size:
        if sequence[index] == target:
            return index
        index += 1
    return None


seq = [0, 2, 4, 6, 8, 7, 5, 9, 1]
target = 8
result = linear_search(seq, target)
if result:
    print("{} at position: {}.".format(target, result))
else:
    print('{} not in sequence.'.format(target))
