import csv
import time
from datetime import datetime
from BubbleSort import bubble_sort
from HeapSort import heap_sort
from QuickSort import quick_sort
from GnomeSort import gnome_sort


def menu():
    print('--------------')
    print('(B)ubblesort', '(H)eapsort', '(Q)uicksort', '(G)nomeSort')
    print('(N)achname', '(P)LZ', '(G)eburtsdatum', '(V)ermögen')
    algorithm = input('Algorithmus?')
    param = input('Wert?')
    print('--------------')
    return param, algorithm


def main():
    unsorted_list = []
    file = open('data/SortSmall.txt')
    data = csv.reader(file, delimiter=',')
    for row in data:
        index = 0
        for index, value in enumerate(row):
            if index == 4:
                row[index] = int(value)
            elif index == 5:
                row[index] = datetime.strptime(value, "%d.%m.%Y")
            elif index == 6:
                row[index] = float(value)
            else:
                pass
            index += 1
        unsorted_list.append(row)
    file.close()

    user_choice = menu()

    if user_choice[1].upper() == 'B':
        start = time.perf_counter()
        sorted_list = bubble_sort(unsorted_list, user_choice[0])
        end = time.perf_counter()
    elif user_choice[1].upper() == 'H':
        start = time.perf_counter()
        sorted_list = heap_sort(unsorted_list, user_choice[0])
        end = time.perf_counter()
    elif user_choice[1].upper() == 'G':
        start = time.perf_counter()
        sorted_list = gnome_sort(unsorted_list, user_choice[0])
        end = time.perf_counter()
    elif user_choice[1].upper() == 'Q':
        sorted_list = None
        start = time.perf_counter()
        if user_choice[0].upper() == 'N':
            print(quick_sort(unsorted_list, 2))
        elif user_choice[0].upper() == 'P':
            print(quick_sort(unsorted_list, 4))
        elif user_choice[0].upper() == 'G':
            print(quick_sort(unsorted_list, 5))
        elif user_choice[0].upper() == 'V':
            print(quick_sort(unsorted_list, 6))
        end = time.perf_counter()
    print(f'Sort: {sorted_list}')
    print(f'Time: {round(end - start, 4)}')


if __name__ == '__main__':
    main()
