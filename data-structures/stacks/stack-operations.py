# Initializing an empty stack
stack = []

# Pushing elements onto the stack
stack.append(10)
print("Pushed 10 onto the stack.")
stack.append(20)
print("Pushed 20 onto the stack.")
stack.append(30)
print("Pushed 30 onto the stack.")

# Printing the top element of the stack
if stack:
    print("Top element of the stack is", stack[-1])
else:
    print("Stack is empty. No top element.")

# Popping elements from the stack
if stack:
    item = stack.pop()
    print("Popped", item, "from the stack.")
else:
    print("Stack is empty. Cannot pop.")
if stack:
    item = stack.pop()
    print("Popped", item, "from the stack.")
else:
    print("Stack is empty. Cannot pop.")

# Checking if the stack is empty
if stack:
    print("Stack is not empty.")
else:
    print("Stack is empty.")

# Printing the size of the stack
stack_size = len(stack)
print("Size of the stack is", stack_size)
