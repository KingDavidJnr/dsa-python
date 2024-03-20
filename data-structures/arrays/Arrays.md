# Array Data Structure

An array is a fundamental data structure used to store a collection of elements, where each element is identified by at least one array index. Arrays are essential for organizing and manipulating data efficiently in computer programming.

## Overview

- **Data Type**: Arrays can hold elements of the same data type. For example, an array of integers, an array of characters, etc.
- **Fixed Size**: Arrays have a fixed size, meaning the number of elements it can hold is determined at the time of declaration and cannot be changed during runtime.
- **Contiguous Memory**: Array elements are stored in contiguous memory locations, allowing for efficient random access to elements using their indices.
- **Zero-Based Indexing**: In most programming languages, array indices start from 0. This means the first element of the array is accessed using index 0, the second element with index 1, and so on.

## Operations

### 1. Accessing Elements

- **Read Operation**: Accessing elements by their index. For example, `array[0]` retrieves the first element of the array.

### 2. Insertion and Deletion

- **Insertion**: Adding elements to the array.
- **Deletion**: Removing elements from the array.

### 3. Searching

- **Linear Search**: Iterating through the array sequentially to find a specific element.
- **Binary Search**: Requires the array to be sorted. It divides the array into halves and compares the target value with the middle element.

### 4. Traversal

- Iterating through all elements of the array, usually done using loops.

### 5. Update

- Modifying the value of an existing element in the array.

## Time Complexity

- **Access**: O(1)
- **Search**: O(n) for linear search, O(log n) for binary search (if the array is sorted)
- **Insertion/Deletion**: O(n) in the worst case (if elements need to be shifted), O(1) if inserting/deleting at the end of the array

## Examples

```python
# Initializing an array
array = [1, 2, 3, 4, 5]

# Accessing elements
print(array[0])  # Output: 1

# Insertion
array.append(6)  # Adding element 6 to the end of the array

# Deletion
del array[0]  # Removing the first element

# Searching
if 3 in array:
    print("Element found")
else:
    print("Element not found")

# Traversal
for element in array:
    print(element)

# Update
array[0] = 10  # Updating the first element to 10
