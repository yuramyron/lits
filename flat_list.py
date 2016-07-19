def flat_the_list (inp_list):
    flat_list = []
    for item in inp_list:
        if type(item) == list:
            sub_list = flat_the_list(item)
            for sub_item in sub_list:
                flat_list.append(sub_item)
        else:
            flat_list.append(item)
    return flat_list

# sample inputs
lists_to_flat = [[1, 2, 3, 4, [5, 6], 7],
                [1, [[2, 3], 4, [[6, 7]]],11],
                ['a', [[],'b', {'key':'val'},['c','d']], 1,2,['e','f',[3,4]],5]]

for inp_list in lists_to_flat:
    print 'Input list: ', inp_list
    res_list = flat_the_list(inp_list)
    print 'Flat list: ', res_list

