def print_max_number(a : int, b : int) -> int:
    sum = a + b
    return sum

print(print_max_number(5, 10))

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(print_max_number(x, y))


def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]



def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes


print(string_to_codes("Hello, World!"))


#Sample of nested functions
#Sample1: Enclosing variable
print("Приклад вкладених (Nested) функцій:")
def outer_func():
    enclosing_var = "Я змінна в функції, що охоплює"

    def inner_func():
        print("Всередині вкладеної функції:", enclosing_var)

    inner_func()

outer_func()


#Sample2:  nonlocal
def func_outer():
    x = 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    return x

result = func_outer()  # 5


#Sample3: Global var
x = 50

def func():
    global x
    print('x дорівнює', x)  # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

func()
print('Значення x складає', x)# Значення x складає 2


######################
#non-fixed number of arguments
#Sample1: *args
print("non-fixed number of arguments")

def print_all_args(*args):
    for arg in args:
        print(arg)

print_all_args(1, 'hello', True)

#Sample2: 
def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))



#Split sentence by words
text = "Even though programming can feel confusing at first, practice makes everything clearer over time. Writing small programs every day helps build real confidence."
words = []
start = 0
print("\n\nSplit sentence by words:")
for indx, char in enumerate(text):
    print(indx, char)
    if char == " ":
        words.append(text[start:indx])
        start = indx + 1
    print(words)

duplicated_words = "I was walking walking through the park park when I suddenly suddenly realized that the sound sound of birds birds and the rustling rustling leaves leaves made me feel feel calm calm and relaxed relaxed even though though I had been been worried worried all morning morning."
