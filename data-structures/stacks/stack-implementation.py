class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Add an element to the top of the stack.
        
        Args:
        - item: The element to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top element from the stack.
        
        Returns:
        - The top element of the stack, or None if the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """
        Return the top element of the stack without removing it.
        
        Returns:
        - The top element of the stack, or None if the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
        - True if the stack is empty, False otherwise.
        """
        return not self.items

    def size(self):
        """
        Return the number of elements in the stack.
        
        Returns:
        - The number of elements in the stack.
        """
        return len(self.items)
