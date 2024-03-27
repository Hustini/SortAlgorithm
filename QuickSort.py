import time
import csv


def quick_sort(list, param):
    left = []
    right = []
    equal = []

    if len(list) > 1:
        pivot = list[-1][param]
        for i in list:
            if i[param] < pivot:
                left.append(i)
            elif i[param] == pivot:
                equal.append(i)
            elif i[param] > pivot:
                right.append(i)

        return quick_sort(left, param) + equal + quick_sort(right, param)
    else:
        return list


def main():
    unsorted_list = []
    file = open('data/SortSmall.txt')
    data = csv.reader(file, delimiter=',')
    for row in data:
        print(row)
        unsorted_list.append(row)
    print(unsorted_list)

    start = time.perf_counter()

    print(quick_sort(unsorted_list, 2))

    end = time.perf_counter()
    print(f'Time: {end - start}')


if __name__ == '__main__':
    main()
