import csv
import time
from BubbleSort import bubble_sort
from HeapSort import heap_sort


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
    print(f'Time: {end - start}')
    print(f'Sorted list: {sorted_list}')



if __name__ == '__main__':
    main()
