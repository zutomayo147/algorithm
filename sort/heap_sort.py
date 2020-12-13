# ヒープソート
def heap_sort(array):
    i = 0
    n = len(array)

    while(i < n):
        # ヒープを構成
        upheap(array, i)
        i += 1

    while(i > 1):
        # ヒープから最大値を取り出し
        i -= 1
        tmp = array[0]
        array[0] = array[i]
        array[i] = tmp

        # ヒープの再構成
        downheap(array, i-1)

# array[n]をヒープ構成部(0～n-1)の最適な位置へ移動


def upheap(array, n):
    while n != 0:
        parent = int((n - 1) / 2)
        if array[n] > array[parent]:
            # 親より大きな値の場合親子の値を交換
            tmp = array[n]
            array[n] = array[parent]
            array[parent] = tmp
            n = parent
        else:
            break

# ルート[0]をヒープ(0～n)の最適な位置へ移動


def downheap(array, n):
    if n == 0:
        return
    parent = 0
    while True:
        child = 2 * parent + 1  # array[n]の子要素
        if child > n:
            break
        if (child < n) and array[child] < array[child + 1]:
            child += 1
        if array[parent] < array[child]:  # 子要素より小さい場合スワップ
            tmp = array[child]
            array[child] = array[parent]
            array[parent] = tmp
            parent = child  # 交換後のインデックスを保持
        else:
            break


# デバッグ
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 3, 2, 1, 4, 3, 4, 5, 0]
    print("before", array)
    heap_sort(array)
    print("after ", array)
