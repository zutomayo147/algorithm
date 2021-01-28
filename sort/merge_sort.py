import random

#統合部


def merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    for i in range(left, right):
        if len(L) == 0:
            A[i] = R.pop(0)
        elif len(R) == 0:
            A[i] = L.pop(0)
        elif L[0] <= R[0]:
            A[i] = L.pop(0)
        else:
            A[i] = R.pop(0)

#分割部


def mergesort(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2
        mergesort(A, left, mid)
        mergesort(A, mid, right)
        merge(A, left, mid, right)
        print(A)


A = [i+1 for i in range(10)]
random.shuffle(A)
print(A)
mergesort(A, 0, len(A))
print(A)
