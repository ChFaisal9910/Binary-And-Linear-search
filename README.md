
## Overview  
This repository contains implementations of two widely used search algorithms: **Binary Search** and **Linear Search**. These algorithms are fundamental in data structures and algorithms and demonstrate different approaches to searching for an element within a list.  

## Purpose of the Code  
The purpose of this code is to provide simple and efficient implementations of search algorithms for a **DSA lab assignment**. These algorithms illustrate the difference between sequential and divide-and-conquer search strategies, helping students understand their applications and time complexities.  

## How to Run the Program  
1. Clone the repository or copy the code to your local machine.  
2. Ensure Python is installed on your system.  
3. Open a Python editor (e.g., VS Code, PyCharm) or a terminal.  
4. Run the program by executing the file containing the code, for example:  
   ```bash  
   python search_algorithms.py  
   ```  
5. Modify the sample input (`arr` and `target`) within the code to test various scenarios.  

## Features  
- **Binary Search**: Efficiently searches for an element in a sorted list using a divide-and-conquer approach.  
- **Linear Search**: Performs a simple, step-by-step search in both sorted and unsorted lists.  
- Easy-to-understand logic with clear examples for testing.  
- Output messages indicate whether the target element was found and its position.  

## Time Complexity  
- **Binary Search**:  
  - Best Case: \(O(1)\) (if the middle element is the target).  
  - Average/Worst Case: \(O(\log n)\) (where \(n\) is the number of elements).  
- **Linear Search**:  
  - Best Case: \(O(1)\) (if the target is the first element).  
  - Average/Worst Case: \(O(n)\) (when the target is near the end or not present).  

## Example Scenarios  
### Binary Search  
Input:  
```python  
arr = [1, 3, 5, 7, 9, 11]  
target = 7  
```  
Output:  
```  
Binary Search: Element located at position 3  
```  

### Linear Search  
Input:  
```python  
arr = [11, 3, 7, 5, 1, 9]  
target = 7  
```  
Output:  
```  
Linear Search: Element found at index 2  
```  

