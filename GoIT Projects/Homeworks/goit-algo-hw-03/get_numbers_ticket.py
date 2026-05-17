import random

def get_numbers_ticket(min, max, quantity):
    # fill the list with the values one by one:
    if min >=1 and max <= 100 and max >= min and quantity <= (max - min):
        # declare empty list 
        lst = []
        while len(lst) != quantity:
            # generate random value
            lst.append(random.randrange(min, max))
            # making values unique in ht elist
            lst = list(set(lst))
            # sorting the list in ascending way
            lst.sort()
        return lst
    else:
        print("Please select positive integer numbers:\nmin >= 1 \nmax <= 100\nquantity <= (max - min)")
    


min = 10
max = 100
quantity = 6
print("Your lottery numbers:\t", get_numbers_ticket(min, max, quantity))