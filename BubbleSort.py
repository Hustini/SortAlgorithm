import time
import csv


def bubble_sort(list, param):
    sorted = False
    while not sorted:
        changed = False
        for i in range(len(list) - 1):
            if list[i][param] > list[i + 1][param]:
                list[i], list[i + 1] = list[i + 1], list[i]
                changed = True
        if not changed:
            sorted = True
    print(f'Sorted list: {list}')


def main():
    unsorted_list = []
    file = open('data/SortSmall.txt')
    data = csv.reader(file, delimiter=',')
    for row in data:
        print(row)
        unsorted_list.append(row)
    print(unsorted_list)

    start = time.perf_counter()

    bubble_sort(unsorted_list, 4)

    end = time.perf_counter()
    print(f'Values in list: {len(unsorted_list)}\nTime: {end - start}')


if __name__ == '__main__':
    main()
