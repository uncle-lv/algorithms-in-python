from typing import List

'''

Time Complexity: O(n^2)
Auxiliary Space: O(1)

''' 

def bubble_sort(arr: List[int]) -> List[int]:
    swapped = False
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # No swap occurs indicating that the array is sorted, just return it
        if not swapped:
            return arr

    return arr
