import csv
import time
from BubbleSort import bubble_sort
from HeapSort import heap_sort
from QuickSort import quick_sort
from GnomeSort import gnome_sort


def menu():
    print('--------------')
    print('(B)ubblesort', '(H)eapsort', '(Q)uicksort', '(G)nomeSort')
    print('(N)achname', '(P)LZ', '(G)eburtsdatum', '(V)ermögen')
    param = input('param?')
    algorithm = input('algorithm?')
    print('--------------')
    return param, algorithm


def main():
    unsorted_list = []
    file = open('data/SortSmall.txt')
    data = csv.reader(file, delimiter=',')
    for row in data:
        unsorted_list.append(row)

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
    print(f'Time: {end - start}')
    print(f'Sort: {sorted_list}')


if __name__ == '__main__':
    unsorted_list = []
    file = open('data/SortSmall.txt')
    data = csv.reader(file, delimiter=',')
    index = 0
    for row in data:
        index = 0
        for index, value in enumerate(row):
            if index == 4:
                row[index] = int(value)
            elif index == 5:
                pass
            elif index == 6:
                row[index] = float(value)
            else:
                pass
            index += 1
        unsorted_list.append(row)
        print(row)
    file.close()
