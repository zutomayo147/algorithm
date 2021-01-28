import time
import pickle
 
mask = 0xff
size = 255
 
def radix_sort(lst):
    length = len(lst)
    tmp = [None for _ in range(length)]
    for bit in range(0, 32, 8):
        count = [0 for _ in range(size+1)]
        for i in range(length):
            count[(lst[i]>>bit) & mask] += 1
        for i in range(size):
            count[i+1] += count[i]
        for i in range(length-1, -1, -1):
            count[(lst[i]>>bit) & mask] -= 1
            tmp[count[(lst[i]>>bit) & mask]] = lst[i]
        for i in range(length):
            lst[i] = tmp[i]
 
with open('sample_data.pkl', 'rb') as f:
    lst = pickle.load(f)
 
start = time.time()
radix_sort(lst)
print("elapsed {} sec".format(time.time() - start))
