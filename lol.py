data_base = []
while True:
    choice = input('''1 создать хранилище
2 записать в хранилище
3 прочитать таблицу
4 выход
:''')

    if choice == '1' :
        data_base.append([])
    if choice == '2' :
        if data_base:
            print('хранилище есть')
            print(f'Доступно {len(data_base)}')
            number = int(input('выберете номер хранилища:')) - 1
            data = input('Данные которые нужно вставить')
            data_base[number].append(data)
            
        else:
            print('пусто')
    if choice == '3' :
        pass
    if choice == '4' :
        break
    print(data_base)
