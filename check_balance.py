def check_element(inp_str, elements):
    result = 'balance found'
    element_open = elements[0]
    element_close = elements[1]
    count = 0
    for ch in inp_str:
        if ch == element_open:
            count += 1
        elif ch == element_close:
            count -=1
            #when we find more closed then were opened we break, e.g ())(
            if count < 0: break
    if count > 0: result = 'no balance: redundant ' + element_open +' found'
    if count < 0: result = 'no balance: redundant ' + element_close +'found '
    return result

result = None
element_types = ['()','{}','[]']
inp_str = '[],(4),3,(({}),{{[4]},{5}})'

for element in element_types:
    #if we are already not balanced - break
    if result != None and result != 'balance found': break
    result = check_element(inp_str, element)

print 'Result:', result