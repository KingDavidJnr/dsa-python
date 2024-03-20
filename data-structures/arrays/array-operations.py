# Initializing an array
array = [1, 2, 3, 4, 5]
print("Original Array:", array)

# Accessing elements
print("\nAccessing Elements:")
print("First Element:", array[0])
print("Last Element:", array[-1])

# Insertion
array.append(6)
print("\nAfter Insertion:", array)

# Deletion
del array[0]
print("\nAfter Deletion:", array)

# Searching
element_to_search = 3
if element_to_search in array:
    print("\nElement", element_to_search, "found in the array.")
else:
    print("\nElement", element_to_search, "not found in the array.")

# Traversal
print("\nTraversal:")
for element in array:
    print(element)

# Update
array[0] = 10
print("\nAfter Update:", array)
