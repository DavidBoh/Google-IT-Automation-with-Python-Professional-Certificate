#!/usr/bin/env python3

iterator = 0 
indexer = 1
my_list = ['a','b','c','d','e','f','g','h','i','j','k','l']
new_list = list()
while iterator < len(my_list):
    if indexer > len(my_list):
        break
    new_list.append(my_list[indexer-1])
    indexer += 1
    new_list.append(my_list[indexer-1])
    indexer += 3
    iterator += 1

    print("completed iteration", iterator)

print(new_list)
