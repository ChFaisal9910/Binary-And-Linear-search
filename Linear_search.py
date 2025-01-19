def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i  
    return -1 


numbers = [15, 3, 8, 7, 12]
search_value = 7
output = linear_search(numbers, search_value)
if output != -1:
    print(f"Linear Search: Element found at index {output}")
else:
    print("Linear Search: Element not found")
