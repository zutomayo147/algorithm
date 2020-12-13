import time
import pickle


def shell_sort(lst):
    print("00:", lst)
    print()
    length = len(lst)
    h = 1
    while h < length / 9:
        h = h * 3 + 1
    while h > 0:
        for i in range(h, length):
            j = i
            while j >= h and lst[j-h] > lst[j]:
                tmp = lst[j]
                lst[j] = lst[j-h]
                lst[j-h] = tmp
                j -= h
        print("{:02}: {}".format(i+1, lst))
        h = int(h / 3)


with open('sample_data.pkl', 'rb') as f:
    lst = pickle.load(f)

start = time.time()
lst = [20, 6, 55, 74, 3, 45, 13, 87, 46, 30]
shell_sort(lst)
print("elapsed {} sec".format(time.time() - start))
