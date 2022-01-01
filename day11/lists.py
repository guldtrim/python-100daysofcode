import random

empty_list = [10, 5, 5]

if 5 in empty_list:
    empty_list.append(-10)
    print(sum(empty_list))