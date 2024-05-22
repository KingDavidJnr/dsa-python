# Stacks Data Structure

In this document, we'll explore the various operations that can be performed on stacks using Python, along with their time and space complexities.

## 1. Push Operation:

The `push` operation adds an element to the top of the stack.

```python
def push(stack, item):
    stack.append(item)
```

**Time Complexity:** O(1) - Constant time complexity because appending an element to the end of a list in Python takes constant time.

**Space Complexity:** O(1) - Constant space complexity as it only requires additional memory for the new element.

## 2. Pop Operation:

The `pop` operation removes and returns the top element from the stack.

```python
def pop(stack):
    if not stack:
        return None
    return stack.pop()
```

**Time Complexity:** O(1) - Constant time complexity because removing the last element from a list in Python takes constant time.

**Space Complexity:** O(1) - Constant space complexity as it doesn't require additional memory.

## 3. Peek/Top Operation:

The `peek` operation returns the top element of the stack without removing it.

```python
def peek(stack):
    if not stack:
        return None
    return stack[-1]
```

**Time Complexity:** O(1) - Constant time complexity because accessing the last element of a list in Python takes constant time.

**Space Complexity:** O(1) - Constant space complexity as it doesn't require additional memory.

## 4. isEmpty Operation:

The `isEmpty` operation checks if the stack is empty.

```python
def isEmpty(stack):
    return not stack
```

**Time Complexity:** O(1) - Constant time complexity because it only checks the length of the stack.

**Space Complexity:** O(1) - Constant space complexity as it doesn't require additional memory.

## 5. Size Operation:

The `size` operation returns the number of elements in the stack.

```python
def size(stack):
    return len(stack)
```

**Time Complexity:** O(1) - Constant time complexity because it only returns the length of the stack.

**Space Complexity:** O(1) - Constant space complexity as it doesn't require additional memory.

---