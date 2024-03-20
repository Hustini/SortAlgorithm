import csv
import time
from BubbleSort import bubble_sort


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
        if user_choice[0].upper() == 'N':
            bubble_sort(unsorted_list, 2)
        if user_choice[0].upper() == 'P':
            bubble_sort(unsorted_list, 4)
        if user_choice[0].upper() == 'G':
            bubble_sort(unsorted_list, 5)
        if user_choice[0].upper() == 'V':
            bubble_sort(unsorted_list, 6)
        end = time.perf_counter()
        print(f'Time: {end - start}')


if __name__ == '__main__':
    main()
