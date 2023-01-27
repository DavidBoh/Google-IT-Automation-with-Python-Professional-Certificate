#!/usr/bin/env python3

"""
Where new_list is a list of an even number of strings. 
For example
new_list = ['a','b','c','d','e','f']
Output will be
result will be [{'name':'a','weight':'b'},{'name':'c','weight':'d'} ... etc]
however we will pass the list of dicts to a json.dump()
And we will store that created list of dicts into a valid json file. 
"""

the_dict = {'name':'',
                'weight':''}
    result = []
    for name, weight, *other in zip(*[iter(new_list)]*2):
        the_dict = {'name':name, 'weight':weight}
        for i in range(0, len(other), 2):
            the_dict[other[i]] = other[i+1]
        result.append(the_dict.copy())

    print(result)
    with open('fruits.json', 'w') as file:
        json.dump(result,file)


