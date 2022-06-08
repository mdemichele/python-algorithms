def balanced_brackets(input):
    """returns whether brackets are balanced or not"""
    # This is our stack to keep track of matching brackets 
    stack = list()
    
    # Iterate through input string 
    for char in input:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        else:
            current = stack.pop(len(stack) - 1)
            if current == "(":
                if char != ")":
                    return False 
            elif current == "[":
                if char != "]":
                    return False 
            else:
                if char != "}":
                    return False
                    
    # If stack is not empty, then brackets are not matching 
    if len(stack) != 0:
        return False
        
    return True
        
# if __name__ == "__main__":
#     answer = balanced_brackets("()")
#     print(answer)