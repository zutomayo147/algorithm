import random


def counting_sort(A, max_num):
    #配列は0スタートのため
    count_list = [0]*(max_num+1)
    for i in A:
        count_list[i] += 1
    i = 0
    for num in range(len(count_list)):
        for c in range(count_list[num]):
            A[i] = num
            i += 1


#要素数15の配列を作成
A = [random.randint(1, 10) for _ in range(15)]
#randomに生成できる整数の最大値をmax_numとしてsortしていく
print(A)
counting_sort(A, 10)
print(A)
