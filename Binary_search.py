def binary_search(arr, value):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = start + (end - start) // 2 
        if arr[middle] == value:
            return middle  
        elif arr[middle] < value:
            start = middle + 1  
        else:
            end = middle - 1  

    return -1  


numbers = [2, 4, 6, 8, 10, 12]
search_value = 8
output = binary_search(numbers, search_value)
if output != -1:
    print(f"Binary Search: Element located at position {output}")
else:
    print("Binary Search: Element not found")
