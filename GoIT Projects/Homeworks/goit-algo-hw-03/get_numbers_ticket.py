import random

def get_numbers_ticket(min, max, quantity):
    # declare empty list 
    lst = []
    # fill the list with the values one by one:
    while len(lst) != quantity:
        # generate random value
        lst.append(random.randrange(min, max, quantity))
        # making values unique in ht elist
        lst = list(set(lst))
        # sorting the list in ascending way
        lst.sort()
    return lst


min = 1
max = 100
quantity = 6
print("Ваші лотерейні числа:", get_numbers_ticket(min, max, quantity))