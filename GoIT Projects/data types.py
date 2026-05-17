#Data types and operations in Python
a = 1
b = int(float(2.5))
c = "test"
d = True
e = []
f = {}
g = ()
h = {()}
print ("Data types:\n\n"+"a: ", a, "type of a: ", type(a))
print("b: ", b, "type of b: ", type(b))
print("c: ", c, "type of c: ", type(c))
print("d: ", d, "type of d: ", type(d))
print("e: ", e, "type of e: ", type(e))
print("f: ", f, "type of f: ", type(f))
print("g: ", g, "type of g: ", type(g))
print("h: ", h, "type of h: ", type(h))

print("\n\nSample:")
volume = float(input("Which fuel volume do you want to charge? "))
price = float(input("Fuel priceper liter: "))
total_cost = volume * price
print("Total cost: ", total_cost)



#String operations
# 1. Робота з регістром (велика/мала літера)
# s.lower()      # всі малі літери
# s.upper()      # всі великі літери
# s.capitalize() # перша літера велика
# s.title()      # кожне слово з великої
# s.swapcase()   # змінює регістр навпаки


# 2. Пошук у рядку
# s.find("a")      # індекс першого входження (-1 якщо нема)
# s.rfind("a")     # з кінця
# s.index("a")     # як find, але помилка якщо нема
# s.count("a")     # кількість входжень


# 3. Перевірки (True/False)
# s.isalpha()   # тільки літери
# s.isdigit()   # тільки цифри
# s.isalnum()   # літери + цифри
# s.isspace()   # тільки пробіли
# s.startswith("py")
# s.endswith("on")


# 4. Розбиття і склеювання
# s.split()        # розбити на список
# s.split(" ")     # по символу
# " ".join(list)   # склеїти в рядок

# 5. Видалення пробілів
# s.strip()   # зліва і справа
# s.lstrip()  # зліва
# s.rstrip()  # справа

# 6. Заміна
# s.replace("a", "b")   # замінити всі "a" на "b"

# 7. Форматування рядків
# f"Hello {name}"
# "Hello {}".format(name)

# 8. Робота з позиціями
# s[0]      # перший символ
# s[-1]     # останній
# s[1:5]    # зріз
# s[::-1]   # розворот рядка
# s[:-1] без останнього елемента

# 9. Довжина рядка
# len(s)

s = "hello, world!"
print("\n\nString:\n\n"+"s: ", s)
print("Length of s: ", len(s))
print("Make it title: ", s.title())
print("How many l counts in the sentence: ", s.count('l')   )
print("s in uppercase: ", s.upper())
print("s in lowercase: ", s.lower())
print("s with replaced 'o' with '0': ", s.replace('o', '0'))
print("s split by comma: ", s.split(','))
print("s splitted by space: "), s.split()
print("   s striped starting and ending spaces   ".strip())
print("s starts with 'Hello': ", s.startswith('Hello'))
print("s ends with 'World!': ", s.endswith('World!'))  
print("s find 'o': ", s.find('o')) #returns the index of the first occurrence of 'o', returns -1 if not found
print("s find 'x': ", s.find('x')) #returns -1 if 'x' is not found
start = 0
end = 12
print(s.find("l", start, end)) # 5 index of found "er"
print(s.index("o")) # те саме як find
print(s.rindex("o")) # те саме як rfind
print("s count 'o': ", s.count('o')) #returns the number of occurrences of 'o' in s     
print("s is alphanumeric: ", s.isalnum()) #returns False because s contains a comma and an exclamation mark
print("s is alphabetic: ", s.isalpha()) #returns False because s contains a comma and an exclamation mark
print("s is digit: ", s.isdigit()) #returns False because s contains letters and punctuation
print("s is whitespace: ", s.isspace()) #returns False because s contains letters and punctuation   
print("s is title: ", s.istitle()) #returns False because s is not in title case    
print("s is lower: ", s.islower()) #returns False because s contains uppercase letters
print("s is upper: ", s.isupper()) #returns False because s contains lowercase letters
print("s is printable: ", s.isprintable()) #returns True because all characters in s are printable
print("s is numeric: ", s.isnumeric()) #returns False because s contains letters and punctuation
print("s is decimal: ", s.isdecimal()) #returns False because s contains letters and punctuation
print("s is identifier: ", s.isidentifier()) #returns False because s contains a comma and an exclamation mark
print("s is space: ", s.isspace()) #returns False because s contains letters and punctuation
print("s is capitalized: ", s.capitalize()) #returns a copy of s with the first character capitalized and the rest lowercased    
print("s is title: ", s.title()) #returns a copy of s with the first character of each word capitalized and the rest lowercased
print("s is swapcase: ", s.swapcase()) #returns a copy of s with uppercase letters converted to lowercase and vice versa

print("First {0}, second {1}, third {0}, fourth {1}.".format(1, 2))
print("First {}, second {} using .format".format("one", "two"))
print("First %s, second %d " % ("one", 2))
# count number of hours, minutes and seconds using integer division and modulus operator
n = 5000
hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60
print("{0} seconds is {1} hours, {2} minutes and {3} seconds.".format(n, hours, minutes, seconds))

#Arithmetic operations
value_one = 2
value_two = 7
value_three = -3.14
sum = 0
print("\n\nArithmetic operations:", sum)
sum += value_one
print("+=", sum)
sum -= value_two
print("-=", sum)
sum /= value_one
print("/=", sum)
sum *= value_two
print("*=", sum)
sum **= value_one
print("**=", sum)
sum //= value_two # // - цілочислене ділення (7:2 = 3)
print("//=", sum)  

print("модуль числа:", value_three , "is abs()", abs(value_three))

print("\n\nComparison and identity operations:\n\n")
sentence_one = "Hello world!"
sentence_two = "Hello " + "world!"

print("\n\nsentence_one: ", sentence_one)
print("sentence_two: ", sentence_two)
print("sentence_one == sentence_two: ", sentence_one == sentence_two) #returns True because the values of sentence_one and sentence_two are the same, even though they are different objects in memory
print("sentence_one is sentence_two: ", sentence_one is sentence_two) #returns False because sentence_one and sentence_two are different objects in memory, even though they have the same value
print("id of sentence_one: ", id(sentence_one))
print("id of sentence_two: ", id(sentence_two))


one_line_text = ("select * "
                "from some_table "
                "where condiiton1 is True "
                "and condition2 is False")
print(one_line_text)

separated_string = "long text can " \
"be texted in " \
"a couple lines"
print(separated_string)

couple_lines_text = """
    poem can be written
    in a couple lines 
   having tabulations
  and spaces
 at the start"""
print(couple_lines_text)

# Tabulations:
test_line = "\v test \v test \v test"
print(test_line)

test_line2 = "\r test \r test \r test"
print(test_line2)

test_line3 = "test \t test \t test"
print(test_line3)

some_list = ["some", "text"] # should be list of strings only
print(", ".join(some_list))

text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 3)
print(new_text)
print(new_text.replace("bird", ""))
print("NextGeneration".removeprefix("Next"))


url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

els = {}
for el in query.split("&"):
    key, value = el.split("=")
    els.update({key: value.replace("+", " ")})
print(els) 


# Translate
sample = "aeiou"
replacement_values = "12345"
trantab = str.maketrans(sample, replacement_values)
#case1:
text = "This is string example"
print(text.translate(trantab))
#case2:
trantab = str.maketrans('', '', sample)
print(text.translate(trantab))

# Search across the string

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end))



#Input
print("\n\nInput:\n\n")
name = input("What is your name? ")
print("Hello, {} !".format(name))
print("Hello, " + name + " !")
print("Hello, %s !" % name)
print(f"Hello, {name} !")



# List operations
# Додавання елементів
# my_list.append(40)      # додає в кінець
# my_list.insert(1, 15)   # вставляє на позицію

# Видалення елементів
# my_list.remove(20)  # видаляє за значенням
# my_list.pop()       # видаляє останній
# my_list.pop(0)      # видаляє за індексом

# Довжина списку
# len(my_list)

# Сортування
# numbers = [3, 1, 4, 2]
# numbers.sort()  # [1, 2, 3, 4]

# Зворотний порядок:
# numbers.sort(reverse=True)

# Перевірка наявності
# if 3 in numbers:
#     print("Є!")

# Зрізи (slicing)
# nums = [0, 1, 2, 3, 4, 5]

# print(nums[1:4])  # [1, 2, 3]
# print(nums[:3])   # [0, 1, 2]
# print(nums[::2])  # [0, 2, 4]

# Перебір списку (loop)
# for item in nums:
#     print(item)

# З індексом:

# for i, val in enumerate(nums):
#     print(i, val)

# Копіювання списку
# a = [1, 2, 3]
# b = a.copy()

# Важливий момент (пастка)
# a = [1, 2, 3]
# b = a

# b.append(4)

# print(a)  # [1, 2, 3, 4] ⚠️
# Тут a і b — це один і той самий список в пам'яті.


My_list = [1, 2, 3, 4, 5]
additional_list = [6, 7, 8, 9, 10]
print("\n\nLists:\n\n"+"My_list: ", My_list)
My_list.append(6)
print("вставлений шостий елемент списка: ", My_list)
My_list.pop()
print("видалений шостий елемент списка: ", My_list)
My_list.pop(3)
print("видалений четвертий елемент списка: ", My_list)
My_list.remove(3)
print("видалений елемент 3 зі списку: ", My_list)
My_list[-2] = 11
print("доданий елемент другий з кінця списку", My_list)
My_list.append(additional_list)
print("доданий додатковий список до My_list: ", My_list)
My_list.extend(additional_list)
print("доданий додатковий список до My_list за допомогою extend: ", My_list)
print("My_list after extend: ", My_list)
print("3d element of My_List sublist ", My_list[3][2])



while My_list:
    My_list.pop()
    print("I remove last element of My_list: ", My_list)

chars = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'a']
numbers = [1, 11, 3, 5, 10, 9, 2, 3, 4, 5]

print(numbers[0])
numbers.insert(0, 0)
print("insert 0 at the beginning of numbers: ", numbers)
print(numbers[0])


print("Index of 'c' in chars: ", chars.index('c'))
chars.insert(chars.index('c'), 'CC')
print("Insert CC in cars list at c index: ", chars)
chars[chars.index('c')] = None 
print("Replace c with None using index: ", chars)
chars[3] = None
print("Replace d with None using index: ", chars)   
print("Count of 'a' in chars: ", chars.count('a'))
print("length of chars: ", len(chars))

print("Sorted copy of numbers list: ", sorted(numbers.copy()))
print("Sorted copy of numbers list in reverse order: ", sorted(numbers, reverse=True), end="\n\n")

numbers.sort()
print("Sort numbers ascending: ", numbers)



numbers.sort(reverse=True)
print("Sort numbers descending: ", numbers)

numbers_copy = numbers.copy()
print("Copy of numbers: ", numbers_copy)

chars.reverse()
print("Reverse of chars: ", chars)

reference_to_nombers = numbers
print("Reference to numbers: reference_to_nombers = numbers : ", reference_to_nombers)

copy_of_numbers = numbers.copy()
print("Copy of numbers: copy_of_numbers = numbers.copy()", copy_of_numbers)

numbers.clear()
print("Type of numbers list: ", type(numbers))
print("clear numbers list: ", numbers)
print("Reference to numbers: ", reference_to_nombers)
print("Copy of numbers: ", copy_of_numbers)

del numbers
#print("Deleted numbers list: ", type(numbers)) #raises NameError because numbers is deleted
print("Reference to numbers: ", reference_to_nombers)


palindrome = [1,2,3,2,1]
print("Is it a palindrome?: ", palindrome == palindrome[::-1]) #check if a list is a palindrome by comparing it to its reverse

print("Check for uniqueness of all elements of list using 'set' : ", len(palindrome) ==len(set(palindrome))) 




# Dictionary operations
my_dict = {
    "name" : "John",
    "age" : 30,
    "city" : "New York",
    "country" : "USA",
}

additional_info = {
    "gender": "male",
    "salary": 50000
}

print("\n\nDictionary:\n\n"+"Name: ", my_dict["name"])

my_dict["e-mail"] = "john.smith@gmail.com"
print("Added e-mail: ", my_dict)
my_dict["age"] = 31
print("Updated age: ", my_dict)
del my_dict["city"]
print("Deleted city: ", my_dict)

print("If this text present in my_dict: " in my_dict)
print("Keys of my_dict: ", my_dict.keys())
print("Values of my_dict: ", my_dict.values())
print("Items of my_dict: ", my_dict.items())    
print("Length of my_dict: ", len(my_dict))
print("Sorted keys of my_dict: ", sorted(my_dict.keys()))

my_dict.update({"age": 32, "country": "USA", "race": "white"})
print("Updated my_dict: ", my_dict)

my_dict.update(additional_info)
print("Updated my_dict with additional_info: ", my_dict)

age = my_dict.get("age")
print("Get age using get method: ", age)

age += 100
print("Age after adding 100: ", age)

my_dict["race"] += " and Caucasian"
print("Race after concatenating : ", my_dict)

city = my_dict.get("city", "City not found")
print("Get city using get method with default value: ", city)

#city = my_dict["city"] # returns KeyError if key is not found
print("Colour: ", my_dict.get("colour", "Colour not found in dictionalry"))



#Set operations
my_set = set()
a = set("Hello")
print("\n\nSet\n\n"+"Set of characters in 'Hello': ", a)

print("numbers_copy as is : ", numbers_copy)
numbers_as_set = set(numbers_copy)
print("Set of numbers as set: ", numbers_as_set)
numbers_as_list = list(numbers_as_set)
print("Set of chars as list: ", numbers_as_list)

numbers_as_set.add(6)
print("Added 6 to numbers_as_set: ", numbers_as_set)
numbers_as_set.remove(3) #видаляє елемент із множини, викликає виняток, якщо такого елемента немає
print("Removed 3 from numbers_as_set: ", numbers_as_set)
numbers_as_set.discard(10) #видаляє елемент із множини, не викликає виняток, якщо такого елемента немає
print("Discarded 10 from numbers_as_set: ", numbers_as_set)
numbers_as_set.discard(100) #видаляє елемент із множини, не викликає виняток, якщо такого елемента немає
print("Discarded 100 from numbers_as_set: ", numbers_as_set)



# Set math operations
set_a = set([1, 2, 3, 4, 5])
set_b = set([4, 5, 6, 7, 8])    
print("\nSet A: ", set_a)
print("Set B: ", set_b)

print("Intersection of A and B: ", set_a.intersection(set_b))
print("Intersection using & operator: ", set_a & set_b) #intersection using & operator
print("Difference of A from B: ", set_a.difference(set_b))
print("Difference of A from B using - operator: ", set_a - set_b) #difference using - operator
print("Symmetric difference of A and B: ", set_a.symmetric_difference(set_b))
print("Symmetric difference of A and B: using ^ operator: ", set_a ^ set_b) #symmetric difference using ^ operator
print("Union of A and B: ", set_a.union(set_b))
print("Union of A and B using | operator: ", set_a | set_b) #union using | operator 

element_1, element_2, element_3, element_4, element_5 = set_a
print("Unpacking set_a into element_1, element_2, element_3, element_4, element_5: ", element_1, element_2, element_3, element_4, element_5) #unpacking set_a into element

print(f"Min value in set_a: {min(set_a)}, \nMax value in set_a: {max(set_a)}") 




#Frozen set operations
frozen_set_a = frozenset([1, 2, 3, 4, 5])
frozen_set_b = frozenset([4, 5, 6, 7, 8])
print("\n\nFrozen set\n\n"+"Frozen Set A: ", frozen_set_a)
print("Frozen Set B: ", frozen_set_b)

print("Intersection of frozen sets A and B: ", frozen_set_a.intersection(frozen_set_b))
print("Intersection of frozen sets A and B using & : ", frozen_set_a  & frozen_set_b) #intersection using & operator
print("Difference of frozen sets A from B: ", frozen_set_a.difference(frozen_set_b))
print("Difference of frozen sets A from B using - : ", frozen_set_a - frozen_set_b) #difference using - operator
print("Symmetric difference of frozen sets A and B: ", frozen_set_a.symmetric_difference(frozen_set_b))
print("Symmetric difference of frozen sets A and B using ^ : ", frozen_set_a ^ frozen_set_b) #symmetric difference using ^ operator
print("Union of frozen sets A and B: ", frozen_set_a.union(frozen_set_b))
print("Union of frozen sets A and B using | : ", frozen_set_a | frozen_set_b) #union using | operator      


#Tuple operations
my_tuple = (1, 2, 3, 4, 5, "Hello", "World", 2, 3.14)
print("\n\nTuple:\n\n"+"My_tuple: ", my_tuple)
print("Index of 3 in my_tuple: ", my_tuple.index(3))
print("Count of 2 in my_tuple: ", my_tuple.count(2))  
print("Length of my_tuple: ", len(my_tuple))
print("Sorted my_tuple: ", sorted(my_tuple, key=str)) #sorting a tuple using sorted function, key=str is used to sort the elements as strings

my_tuple_2 = 1, "Hello", 3.14 #tuple can be created without parentheses, but it is recommended to use them for better readability
print("My_tuple_2: ", my_tuple_2)
print("Sorted my_tuple in reverse order: ", sorted(my_tuple, key=str, reverse=True)) #sorting a tuple in reverse order using sorted function, key=str is used to sort the elements as strings
print("First element of my_tuple: ", my_tuple[0])

#Tuples can be used as keys in dictionaries because they are immutable, while lists cannot be used as keys because they are mutable.
points = {
    (0, 0): "O",
    (1, 1): "A",
    (2, 2): "B"
}
print("Points dictionary having key as tule: ", points)
print("Value of key (1, 1) in points dictionary: ", points.get(1, 1))  

sample_tuple = (1, 2, [8, 9, 10], 3)
print(type(sample_tuple), sample_tuple)
sample_tuple[2].append(True)
print("Modified sample_tuple: ", sample_tuple) #the list inside the tuple is modified, but the tuple itself is not modified because it is immutable, the reference to the list inside the tuple



#Slice operations
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n\nSlice\n\n"+"My_list: ", my_list)
print("Slice of my_list from index 2 to 5: ", my_list[2:6]) #slice from index 2 to 5, index 6 is not included
print("Slice of my_list from index 0 to 5 with step 2: ", my_list[0:6:2]) #slice from index 0 to 5 with step 2, index 6 is not included
print("Slice of my_list from index 5 to the end: ", my_list[5:])
print("Slice of my_list from the beginning to index 5: ", my_list[:6]) #slice from the beginning to index 5, index 6 is not included
print("Slice of my_list with step 3: ", my_list[::3]) #slice with step 3, from the beginning to the end
print("Slice of my_list in reverse order: ", my_list[::-1]) #slice in reverse order, from the end to the beginning  

my_list_of_lists = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 8, 9, 10]
print("my_list_of_lists: ", my_list_of_lists)
print("my_list_of_lists from second list, slice from third elementtill fifth: ", my_list_of_lists[1][2:4])
print("First element from the end of second sub-list of my_list_of_lists: ", my_list_of_lists[1][-1], my_list_of_lists.index(my_list_of_lists[1][-1]))#returns the index of the last element of the second list in my_list_of_lists