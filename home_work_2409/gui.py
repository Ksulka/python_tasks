def add_contact():
    name = input('Введите имя контакта: ')
    about = input('Введите описание контакта: ')
    number = input('Введите номер контакта: ')
    col = name + ', ' + about + ', ' + number + ';'
    return col

def find_contact():
    name = input('Введите имя контакта: ')
    return name

def action():
    valid = False
    while not valid:
        act = input('Введите действие (с мал.буквы): [read, write, find or delete] -->  ')
        if act == 'read' or act == 'write' or act == 'find' or act == 'delete':
            valid = True
            return act
        else:
            print("Некорректный ввод.")
    
def path_file():
    path = input('Введите путь: ')
    return path