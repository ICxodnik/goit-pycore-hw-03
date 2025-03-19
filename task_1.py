import datetime

def get_days_from_today(date: str)-> int | None:
    
    try:
        input_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except Exception as e:
        print(f"Помилка при форматуванні дати")
        return None 

    today = datetime.date.today()
    return (today - input_date ).days

print(get_days_from_today('2020-10-09'))
print(get_days_from_today('невірна дата'))