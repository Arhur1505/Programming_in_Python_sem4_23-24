from datetime import datetime

def calculate_average_age(file_path, strict_mode=True):
    '''Funkcja licząca średnią'''
    valid_dates = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                parts = line.strip().split()
                if len(parts) != 3:
                    raise ValueError("Niepoprawny format danych")
                
                day, month, year = map(int, parts)
                
                try:
                    date_obj = datetime(year, month, day)
                except ValueError:
                    raise ValueError("Niepoprawna data")
                
                valid_dates.append(date_obj)
            except ValueError as e:
                if strict_mode:
                    raise e
                else:
                    print(f"Ignorowanie niepoprawnej linii: {line.strip()}")
                    continue

    if valid_dates:
        today = datetime.today()
        total_age = sum((today - date_obj).days // 365 for date_obj in valid_dates)
        average_age = total_age / len(valid_dates)
        return average_age
    else:
        raise ValueError("Program wykonał się")


