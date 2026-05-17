import re

def normalize_phone(phone_number):
    # remove all spaces at start and end of the string
    num = phone_number.strip()
    
    #remove extra symbols
    pattern = r"[^\d]"
    num = re.sub(pattern, '', phone_number)


    # if no 38 add at the start
    pattern2 = r"^(?!38)\d+$"
    result = "+38" + num
    num = re.sub(pattern2, result, num)


    # if there is 38 add at the start
    pattern2 = r"^(?=38)\d+$"
    result = "+" + num
    num = re.sub(pattern2, result, num)

    return num



numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

for i in numbers:
    print(normalize_phone(i))