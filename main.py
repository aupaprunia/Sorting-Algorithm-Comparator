import random

from heap_sort import heapsort
from bubble_sort import bubblesort
from insertion_sort import insertion
from regular_quick_sort import quick_sort_main
from merge_sort import mergesort
from selection_sort import selection
from three_median_quick_sort import quick_sort_3_median_main

def main():
    print("\nChoose a sorting algorithm:\n")
    print("1.Quick sort using 3 medians")
    print("2.Bubble Sort")
    print("3.Heap Sort")
    print("4.Insertion Sort")
    print("5.Merge Sort")
    print("6.Regular Quick Sort")
    print("7.Selection Sort")
    sorting_algo = int(input("\nEnter the corresponding number to choose the algorithm: "))

    sorting_algo_map = {1: quick_sort_3_median_main, 2: bubblesort, 3: heapsort, 4: insertion, 5: mergesort, 6: quick_sort_main, 7: selection}

    if sorting_algo not in sorting_algo_map:
        print("\nINVALID CHOICE. PLEASE START OVER")
        main()

    print("\nWhat type of input would you like to give?\n")
    print("1.Randomly generated (between -1000-1000)")
    print("2.I'll enter the numbers myself!")
    input_type = int(input("\nEnter the corresponding number to choose the input type: "))

    input_arr = []

    if input_type == 1:
        numbers_to_generate = int(input("\nHow many numbers would you like to generate (Max 2000 numbers)- "))
        if numbers_to_generate > 2000:
            numbers_to_generate = 2000
        input_arr = list(random.sample(range(-1000, 1000), numbers_to_generate))
    
    elif input_type == 2:
        print("\nEnter the number you would like to sort and press ENTER after each.\nAfter you have entered all the numbers press #\n(Invalid inputs will be ignored)")
        ele = ""
        while ele != "#":
            ele = input("Enter a number: ")
            try:
                input_arr.append(int(ele))
            except:
                pass
    
    else:
        print("INVALID CHOICE. PLEASE START OVER.")
        main()

    print(f"\nThe list of numbers to be sorted is {input_arr}")
    
    result = sorting_algo_map[sorting_algo](input_arr)
    print(f"\nThe sorted numbers are {result}")

if __name__ == "__main__":
    main()