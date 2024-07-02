class Stack:
    def __init__(self):
        self.stack = []
        
    def switch_example(self, argument):
        if argument == 1:
            return self.is_empty()
        elif argument == 2:
            self.push()
        elif argument == 3:
            self.pop()
        elif argument == 4:
            return self.peek()
        else:
            return "Invalid input"

    def is_empty(self):
        return len(self.stack) == 0

    def push(self):
        a = int(input("Input the element to be inserted: "))
        self.stack.append(a)
        return print("Element", a, "has been pushed onto the stack")


    def pop(self):
        if not self.is_empty():
            b = self.stack.pop()
            print("Popped element:", b)
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.stack)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    size = int(input("Size of the stack: "))
    print("1. Check if the stack is empty")
    print("2. Push elements into the stack")
    print("3. Pop elements from the stack")
    print("4. Peek element")
    argument = int(input("Enter the operation to be performed: "))
    print(stack.switch_example(argument))
