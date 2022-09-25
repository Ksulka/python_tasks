import gui

def read_file(path : str):
    with open(path,encoding = 'utf-8', mode = 'r') as file:
        print(file.read())

def write_in_file(path : str):
    with open(path,encoding = 'utf-8', mode = 'a') as file:
        file.write(f'{gui.add_contact()}\n')

def find_in_file(path : str):
    with open(path,encoding = 'utf-8', mode = 'r') as file:
        f = file.read().split(';')
        f_name = gui.find_contact()
        for i in f:
            if f_name in i:
                print(i)

def delete_in_file(path : str):
        with open(path,encoding = 'utf-8', mode = 'r+') as file:
            f = file.read()
            f = f.split(';')
            f_name = gui.find_contact()
            for i in f:
                if f_name in i:
                    f.remove(i)
                    break
        with open(path,encoding = 'utf-8', mode = 'w') as file:
            file.write(';'.join(f))