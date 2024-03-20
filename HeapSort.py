
CHOICE = {'N':2,
          'P':4,
          'G':5,
          'V':6}

def heapify(arr, n, i, sort_by):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i][sort_by] < arr[left][sort_by]:
        largest = left

    if right < n and arr[largest][sort_by] < arr[right][sort_by]:
        largest = right

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])

        heapify(arr, n, largest, sort_by)


def heap_sort(arr, col):
    n = len(arr)
    sort_by = CHOICE[col]


    for i in range(n // 2, -1, -1):
        heapify(arr, n, i, sort_by)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0, sort_by)

    return arr