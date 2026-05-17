# Data flow control
# Умовні оператори (if-elif-else)
# Sample 1: 
print("Conditional statements (if-elif-else)")
print("Задача: перевірити, чи є у користувача гроші на банківському рахунку")


money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")

#Sample2:
result = None
if result:
    print(result)
else:
    print("Result is None, do something")

#Sample3: 
print("Задача: перевірити, чи достатньо грошей для покупки товару")
amount = 0.7 + 0.6
if round(amount, 1) == 1.3: # 1.3 == 1.3
    #if amount == 1.3: # 1.3000000000000002 == 1.3
    print("Amount is enough for purchase")
else:
    print("Amount is not enough for purchase")


user_name = input("Enter your name: ")

if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!")



a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False


# FizzBuzz
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)   


#Тернарний оператор 
#Sample 1:
print("Ternary operator (conditional expression)")

is_nice = True
state = "nice" if is_nice else "not nice"
print(state)


#Sample 2:
some_data = None
msg = some_data or "Не було повернено даних"
print(msg)


# Match-case statement (Python 3.10+)
#Sample 1:

print("Match-case statement")
fruit = "apple"

match fruit:
    case "apple" if fruit == "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _ if fruit != "grape": # Універсальний випадок, якщо жоден з попередніх не збігся
        print("Unknown fruit, but it's not a grape.")
    case _:
        print("Unknown fruit.")

#Sample 2:
point = (0, 1)

match point: 
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, 0):
        print(f"X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
    case _:
            print("Unknown point")

#Sample 3 :
pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")

#Sample: which day it is:
def recognise_day(num):

    match num:
        case 1 | 2 | 3 | 4 | 5:
            return "Business day"
        case 6 | 7:
            return "Weekend"
        case _:
            return "Please enter a number from 1 to 7."
        
try: 
    digit = int(input("Enter a digit: "))
    print(recognise_day(digit))
except ValueError:
    print("Please enter a valid integer.")


# For loop with else
print("For loop with else")
sentence = "This day is wonderful!"

total_chars = len(sentence)
spaces = 0

for char in sentence:
    if char == " ":
        spaces += 1
else:
    print(f"Total characters: {total_chars}")
    print(f"Spaces: {spaces}")  

#Range in for loop
print("Range in for loop:")
for i in range(2, 10):
    print(i)



#Enumerate in for loop
print
some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)


#Zip in for loop
#Sample1:
print("Zip in for loop")
list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)

#Sample2:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

for number, letter in zip(list1, list2):
    print(number, letter)




# Loop inside a dictionary
print("\n\nLoop inside a dictionary")
#Sample1: 
numbers = {
    1: "one",
    2: "two",
    3: "three"
} 
for key, value in numbers.items():
    print(f"{key}: {value}")

#Sample2: 
for key in numbers.keys():
    print(key)

#Sample3:
for val in numbers.values():
    print(val)


#Exception handling
print("\n\nException handling")
#Sample1:
print("Exception handling")
val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")


#Sample2:
age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number, type a number:")
    print("-"*40)

#Sample3: 

def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)

example_function(1, 2, 3, name="Alice", age=25)


#Unpacking 
print("\n\nUnpacking")
#Sample1: 
my_list = [1, 2, 3]
a, _, c = my_list
print(a)  # 1
print(_)  # 2
print(c)  # 3

d, *rest = my_list

print(d)     # 1
print(rest)  # [2, 3]

#Sample2:
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

person_info = {"name": "Alice", "age": 25}
greet(**person_info)


#Recursion
print("\n\nRecursion")
# Рекурсія — це коли функція викликає сама себе, щоб розв’язати задачу по частинах. 
# Звучить страшно, але ідея дуже проста.

# Уяви, що тобі треба пояснити слово зі словника:

# ти відкриваєш визначення
# якщо там є незнайоме слово — шукаєш його теж у словнику
# і так далі, поки не дійдеш до простих слів, які вже розумієш




#Sample1:


# factorial(4)
# = 4 * factorial(3)
# = 4 * 3 * factorial(2)
# = 4 * 3 * 2 * factorial(1)
# = 4 * 3 * 2 * 1
# = 24


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120  