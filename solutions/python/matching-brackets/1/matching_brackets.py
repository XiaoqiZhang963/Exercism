def is_paired(input_string):
    match = {')':'(',']':'[','}':'{'}
    stack = []
    for char in input_string:
        if char in '{[(':
            stack.append(char)
        elif char in ')]}':
            if stack == []:
                return False
            if stack.pop() != match[char]:
                return False
    
    return stack == []
   
            
        
    
            
        
