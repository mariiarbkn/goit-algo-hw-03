import random

def get_numbers_ticket(min_value, max_value, quantity):
    if min_value < 1 or max_value > 1000:
        return []
    if quantity > (max_value - min_value + 1):
        return []

    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
