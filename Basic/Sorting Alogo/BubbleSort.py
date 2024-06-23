def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to detect any swap
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to
