# Description: This program checks if the brackets in an expression are balanced or not.

def is_balanced(expression):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            print(opening_brackets.index(stack.pop()))
            print(closing_brackets.index(char))
            print(not stack)
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False
    print(stack)
    return not stack

# Example usage:
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
  
    expression = input("Enter an expression with brackets: ")
    if is_balanced(expression):
        print("The brackets are balanced.")
    else:
        print("The brackets are not balanced.")
