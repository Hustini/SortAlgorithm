CHOICE = {'N': 2,
          'P': 4,
          'G': 5,
          'V': 6}


def gnome_sort(arr, col):
    n = len(arr)
    sort_by = col
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index][sort_by] >= arr[index - 1][sort_by]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr


