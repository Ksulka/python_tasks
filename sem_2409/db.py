def writer(data):
    with open('db.txt', 'a') as file:
        file.writelines(f'{data}\n')