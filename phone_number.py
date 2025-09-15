import re

def normalize_phone(phone_number):
    digits = re.sub(r'\D', '', phone_number)
    if digits.startswith('380'):
        return '+' + digits
    elif digits.startswith('0'):
        return '+38' + digits
    else:
        return '+' + digits

# Приклади використання
phones = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

for p in phones:
    print(normalize_phone(p))
