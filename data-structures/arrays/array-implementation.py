class Array:
    """
    Array Data Structure Implementation
    
    This class represents a one-dimensional array data structure.
    An array is a collection of elements stored at contiguous memory locations.
    The size of the array is fixed upon initialization.
    
    Attributes:
        size (int): The size of the array.
        capacity (int): The maximum capacity of the array.
        data (list): List to store the elements of the array.
    """
    
    def __init__(self, size):
        """
        Initialize the array with a specified size.
        
        Args:
            size (int): The size of the array.
        """
        self.size = size
        self.capacity = size
        self.data = [None] * size
        
    def __len__(self):
        """
        Return the length of the array.
        
        Returns:
            int: The number of elements currently stored in the array.
        """
        return self.size
    
    def __getitem__(self, index):
        """
        Get the value at a specified index.
        
        Args:
            index (int): The index of the element to retrieve.
            
        Returns:
            object: The value stored at the specified index.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of range")
    
    def __setitem__(self, index, value):
        """
        Set the value at a specified index.
        
        Args:
            index (int): The index of the element to set.
            value (object): The value to store at the specified index.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")
    
    def __iter__(self):
        """
        Return an iterator to iterate over the elements of the array.
        
        Returns:
            iterator: An iterator to iterate over the elements of the array.
        """
        return iter(self.data)
    
    def __str__(self):
        """
        Return a string representation of the array.
        
        Returns:
            str: A string representation of the array.
        """
        return "[" + ", ".join(str(item) for item in self.data) + "]"


# Example usage
if __name__ == "__main__":
    # Creating an array of size 5
    arr = Array(5)
    
    # Inserting values into the array
    for i in range(len(arr)):
        arr[i] = i + 1
    
    # Printing the array
    print("Array:", arr)
    
    # Accessing elements of the array
    print("First Element:", arr[0])
    print("Last Element:", arr[len(arr) - 1])
    
    # Modifying an element
    arr[2] = 10
    print("Modified Array:", arr)
