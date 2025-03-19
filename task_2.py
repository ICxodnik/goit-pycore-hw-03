import random

MAX_VALUE = 1000
MIN_VALUE = 1
MAX_AMOUNT = 1_000_000

def get_numbers_ticket(min: int, max: int, quantity:int) -> int|str:
    if(min < MIN_VALUE):
        print(f"\nМінімальне значення нижче встановленого діапазону: {min}")
        return ""
    
    if(max > MAX_VALUE):
        print(f"\nМаксимальне значення вище встановленого діапазону: {max}")
        return ""
    
    if(max == min):
        print("\nМаксимальне та мінімальне значення не можуть бути рівними")
        return "" 

    if(max < min):
        print(f"\nМаксимальне значення не може бути меньше мінімального: {max} < {min} ")
        return "" 
    
    if(quantity < 1):
        print(f"\nВибірка меньше одиниці: {quantity} елементів")
        return "" 
    
    if(quantity > MAX_AMOUNT):
        print(f"\nВибірка занадто велика: {quantity} елементів")
        return "" 

    valid_range = range(min, max + 1)

    if(quantity > len(valid_range)):
        print("\nКількість вибраних унікальних значень не може бути більше набору значень")
        print(f"min:{min} \nmax:{max} \nquantity:{quantity}")
        return ""

    result = random.sample(valid_range, k=quantity)
    result.sort()
    return result


def test(number_of_tests: int):

    while number_of_tests > 0:
        min_value = random.randint(0,10)
        #max_value = random.randint(0,10)
        max_value = random.randint(min_value, 50)
        quantity = random.randint(0,10)
        print(get_numbers_ticket(min_value, max_value, quantity))
        number_of_tests -= 1

test(1001)