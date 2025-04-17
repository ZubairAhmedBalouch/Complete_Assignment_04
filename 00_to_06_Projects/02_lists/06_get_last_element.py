def get_last_element(lst):
    # Method 1: Using index length - 1
    print("Method 1 - Using len(lst) - 1:", lst[len(lst) - 1])
    
    # Method 2: Using negative index -1
    print("Method 2 - Using lst[-1]:", lst[-1])
    
    # Method 3: Using pop() method (this removes the last element)
    print("Method 3 - Using pop():", lst.pop())

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    get_last_element(lst)
    print("List after pop():", lst)  # Will show the list after the last element is removed
