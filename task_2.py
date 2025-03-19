import random

def get_numbers_ticket(min: int, max: int, quantity:int) -> int:
    if(min < 1):
        print("\nМінімальне значення нижче встановленого діапазону")
        return ""
    
    if(max > 1000):
        print("\nМаксимальне значення вище встановленого діапазону")
        return ""
    
    if(max == min):
        print("\nМаксимальне та мінімальне значення не можуть бути рівними")
        return "" 

    if(max < min):
        print("\nМаксимальне значення не може бути меньше мінімального")
        return "" 

    valid_range = range(min, max + 1)

    if(quantity > len(valid_range)):
        print("\nКількість вибраних унікальних значень не може бути більше набору значень")
        return ""

    result = random.sample(valid_range, k=quantity)
    result.sort()
    return result


def test(number_of_tests: int):

    while number_of_tests > 0:
        
        min_value = random.randint(0,10)
        max_value = random.randint(0,10)
        quantity = random.randint(0,10)
        print(get_numbers_ticket(min_value, max_value, quantity))
        number_of_tests = number_of_tests - 1

test(1001)