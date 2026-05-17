import re

# Positive look ahead ?<= means find the pattern just after the symbol $
string = "Price: $120"
pattern = "(?<=\$)\d+"
result = re.findall(pattern, string)
#print(result)


# Positibe lookahead ?=
# password check
# ^ - start of the string
# (?=.*[A-Z]) - there is an uppercase
# (?=.*[a-z]) - there is a lowercase
# (?=.*\d) - there is a digit
# (?=.*\W) - there is a special symbol
# .{8,} - string consists at least of 8 symbols
# $ - end of string

string = "Iskdfh872@#$90-097!"
pattern = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{8,}$"
result = re.findall(pattern, string)
print(result)



# Parsing HTML
# Проблема regex для HTML:
# HTML вкладений
# regex погано працює з рекурсивними структурами
# ламається на:
# <div><span></span></div>
# Тому використовують:
# HTML parser
# DOM parser
# BeautifulSoup
# lxml
# browser parser



# Backreference
#r означає "сирий" рядок (raw string), який каже Python ігнорувати 
# спеціальні символи такі як \n, \t тощо, оскільки це рядок для регулярних виразів.

print(re.findall(r"(\w+)\s+\1", "hello hello"))


# Search -  знаходить перше значення
string = "Вивчення Python може бути веселим."
pattern = "\w+n може"
new_string = re.search(pattern, string, re.IGNORECASE) # нечутливий до регістру
print(new_string)

if new_string:
    print("Знайдено:", new_string.group())




# Grouping

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)


# Зберегти роздільники

s = "one,two;three"
result = re.split(r"([,;])", s) # Коли regex у (), split зберігає роздільники.
print(result)



# Прибрати порожні елементи
s = "apple,,,banana;;orange"
st = re.split(r"\W+", s)
st = [x for x in st if x]
print(st)