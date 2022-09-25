def get_value():
    while True:
        try:
            data = int(input("Введите число: "))
        except:
            print("Вы ввели не число. Попробуйте снова: ")
        return data

def print_result(data, title):
    print(f'{title} {data}')

def action():
    return input('Какое действие [+; -; *; /], введите символ: ')