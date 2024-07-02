#!/usr/bin/env python


def main():
    expression = "10 1 +"
    
    # convert our expression to a list data structure
    array = expression.split()
    array = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    stack = []
    result = 0
    for token in array:
        
        # check if the operator is an addition operator
        if token == '+':
            if len(stack) >= 2:
                result = stack[len(stack)-2] + stack[len(stack)-1]
                stack.pop()
                stack.pop()
                stack.append(result)
        elif token == '-':
            if len(stack) >= 2:
                result = stack[len(stack)-2] - stack[len(stack)-1]
                stack.pop()
                stack.pop()
                stack.append(result)
        elif token == '*':
            if len(stack) >= 2:
                result = stack[len(stack)-2] * stack[len(stack)-1]
                stack.pop()
                stack.pop()
                stack.append(result)
        elif token == '/':
            if len(stack) >= 2:
                result = round(stack[len(stack)-2] / stack[len(stack)-1])
                stack.pop()
                stack.pop()
                stack.append(result)
        else:
            # this is not an operator
            stack.append(int(token))
    # print the element at the top of the stack
    print(stack[len(stack)-1])
if __name__ == '__main__':
    main()