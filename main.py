class Progg:
    #Программа
    def __init__(self, id, nameP, FileSize, ExeDifficultRating, comp_id):
        self.id = id
        #Наименование программы
        self.nameP = nameP
        #Размер файлов программы
        self.FileSize = FileSize
        #Рейтинг нагрузки на ЦП при исполнении программы
        self.ExeDifficultRating = ExeDifficultRating
        self.comp_id = comp_id


class Comp:
    #Компьютер
    def __init__(self, id, nameComp):
        self.id = id
        self.nameComp = nameComp


class ProggComp:
    #Программы компьютеров
    #для реализации связи многие-ко-многим
    def __init__(self, comp_id, progg_id):
        self.comp_id = comp_id
        self.progg_id = progg_id


# Программы
proggrms = [
    Progg(1, 'PyCharm 20.1', 3145.2, 6, 1),
    Progg(2, 'VS 2017', 7894.2, 5, 3),
    Progg(3, 'SQL Server 2017', 4567.3, 7, 10),
    Progg(4, 'Google Chrome', 411.8, 4, 10),
    Progg(5, 'Блокнот', 23.3, 1, 1),
    Progg(6, 'Server Builder 1.3', 2342.45, 4, 2),
    Progg(7, 'Command Builder 23.4.3', 1204.4, 2, 20),
    Progg(8, 'Server Viewer', 457.3, 6, 20),
    Progg(9, 'Comp Manager 2017', 9874.2, 9, 2),
    Progg(10, 'Command Starter 2.0', 365.54, 5, 30),
    Progg(11, 'ActivityView Manager 2017', 4816.4, 4, 3),
    Progg(12, 'UniversalDo 2.1', 412.56, 8, 30),
    Progg(13, 'EmergencySwitcher', 1234.5, 2, 40),
    Progg(14, 'HelpCallerServer', 220.4, 3, 4),
]

# Компьютеры
comps = [
    Comp(1, "Компьютер ауд. 362"),
    Comp(2, 'Компьютер сервер по ауд. 362'),
    Comp(3, 'Компьютер админ. по сев. крылу'),
    Comp(4, 'Компьютер админ. контроль ГЗ'),
    Comp(10, 'Восмогательная ЭВМ'),
    Comp(20, 'Вспомогательный сервер'),
    Comp(30, 'Резервный админ. по сев. крылу'),
    Comp(40, 'Резервный для админ. контроля ГЗ'),
]

progg_comps = [
    ProggComp(1, 1),
    ProggComp(1, 2),
    ProggComp(1, 3),
    ProggComp(1, 4),
    ProggComp(1, 5),
    ProggComp(2, 6),
    ProggComp(2, 7),
    ProggComp(2, 8),
    ProggComp(2, 9),
    ProggComp(3, 10),
    ProggComp(3, 11),
    ProggComp(3, 12),
    ProggComp(4, 13),
    ProggComp(4, 14),
    ProggComp(10, 1),
    ProggComp(10, 2),
    ProggComp(10, 3),
    ProggComp(10, 4),
    ProggComp(10, 5),
    ProggComp(20, 6),
    ProggComp(20, 7),
    ProggComp(20, 8),
    ProggComp(20, 9),
    ProggComp(30, 10),
    ProggComp(30, 11),
    ProggComp(30, 12),
    ProggComp(40, 13),
    ProggComp(40, 14),
]


def main():
    #Реализация связи один-ко-многим
    one_to_many = [(p.comp_id , p.nameP, p.FileSize, p.ExeDifficultRating, c.nameComp)
                   for c in comps
                   for p in proggrms if p.comp_id == c.id]

    #Решение задания А1
    #Выберем те компьютеры, у которых в названии есть "админ." и выведем их наименование
    #и наименование уставновленных на них программ
    print('\nЗадание А1\n')
    res_1 = ''
    for i in one_to_many:
        if "админ." in i[4]:
            res_1 = res_1 + str(i[4]) + ' с установленной программой: ' + str(i[1]) + '\n'

    print(res_1)

    #Решение задания А2
    #Выберем для каждого компьютера средний размер файлов программы и выведем эти данные,
    #предварительно отсортировав
    print("\nЗадание А2:\n")
    c_prog_all = list()
    for c in comps:
        #Выберем все программы установленные на рассматриваемом компьютере
        progList = list(filter(lambda x: c.id == x[0], one_to_many))
        c_prog = 0
        #Рассматривая каждый элемент списка всех программ компьютера
        for item in progList:
            #Выбор значения количества файлов программы
            p = item[2]
            c_prog = c_prog + p
        #Находим среднее значение размеров файлов
        c_prog = round(c_prog / len(progList), 2)
        #Добавляем найденное среднее значение в список для вывода данных
        c_prog_all.append((c.nameComp, c_prog))
    for item in sorted(c_prog_all, key=lambda x: x[1]):
        print("Для компьютера: {0}, в среднем размер файла {1} MB".format(item[0], item[1]))



    #Реализация связи многие-ко-многим
    many_to_many_temp = [(c.nameComp, cp.comp_id, cp.progg_id)
                            for c in comps
                            for cp in progg_comps
                            if c.id == cp.comp_id]
    many_to_many = [(p.nameP, p.FileSize, p.ExeDifficultRating, nameComp)
                         for nameComp, compId, proggId in many_to_many_temp
                         for p in proggrms
                         if p.id == proggId]


    #Решение задания А3:
    #Выберем данные из составленных связей многие-ко-многим, рассмотрим те программы,
    #название которых начинается с буквы "C" и имена компьютеров
    print("\nЗадание А3:\n")
    res_3 = ''
    for i in many_to_many:
        str3 = i[0]
        for k in range(len(str3)):
            if k == 0 and str3[k] == 'C':
                res_3 = res_3 + 'Программа: ' + str3 + ', установленная на компьютере: ' + str(i[3]) + '\n'
                break
            else:
                break
    print(res_3)


if __name__ == '__main__':
    main()
