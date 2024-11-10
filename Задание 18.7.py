import random
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1,5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
    {students_marks[student]}''')
    print()
print('''Список команд:
         1. Добавить оценку ученика по предмету
         2. Удалить оценку ученика по предмету
         3. Редактировать оценку ученика по предмету
         4. Вывести средний балл по всем предметам по каждому ученику
         5. Вывести средний балл по каждому предмету у определенного ученика
         6. Вывести все оценки по всем ученикам
         7. Вывести все оценки у определенного ученика
         8. Добавить ученика
         9. Выход из программы''')
print()


while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys() and mark >=1 and mark <=5:
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета либо оценка выходит за диапазон допустимых значений')


    elif command == 2:
        print('2. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(students_marks[student])
            class_ = input('Введите предмет по которому нужно удалить оценку: ')
            if class_ in students_marks[student].keys():
                delmark = int(input('Введите оценку, которую нужно удалить: '))
                if delmark in students_marks[student][class_]:
                    students_marks[student][class_].remove(delmark)
                    print(f'У ученика {student} по предмету {class_} удалена оценка {delmark}')
                    print(f'''Актуальные оценки по предметам у ученика {student}
{students_marks[student]}''')
                else:
                    print(f'У ученика {student} по предмету {class_} нет данной оценки')
            else:
                print(f'Данного предмета нет в списке')
        else:
            print(f'Этого ученика нет в списке')


    elif command == 3:
        print('3. Редактировать оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(students_marks[student])
            class_ = input('Введите предмет по которому нужно отредактировать оценку: ')
            if class_ in students_marks[student].keys():
                mark = int(input('Введите оценку которую нужно отредактировать: '))
                if mark in students_marks[student][class_]:
                    redmark = int(input('На какую оценку нужно отредактировать: '))
                    index = students_marks[student][class_].index(mark)
                    students_marks[student][class_].pop(index)
                    students_marks[student][class_].insert(index, redmark)
                    print(f'У ученика {student} по предмету {class_} отредактирована оценка {mark} на {redmark}')
                    print(f'''Актуальные оценки по предметам у ученика {student}
{students_marks[student]}''')
                else:
                    print(f'У ученика {student} по предмету {class_} нет данной оценки')
            else:
                print(f'Данного предмета нет в списке')
        else:
            print(f'Этого ученика нет в списке')


    elif command == 4:
        print('4. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum//marks_count}')


    elif command == 5:
        print('5. Вывести средний балл по каждому предмету у определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
        else:
            print(f'Этого ученика нет в списке')


    elif command == 6:
        print(f'6. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')


    elif command == 7:
        print('7. Вывести все оценки у определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
        else:
            print(f'Этого ученика нет в списке')


    elif command == 8:
        print('8. Добавить ученика')
        new_student = input('Введите имя ученика: ')
        students.append(new_student)
        for new_student in students:
            students_marks[new_student] = {}
            for class_ in classes:
                marks = [random.randint(1, 5) for i in range(3)]
                students_marks[new_student][class_] = marks
        print(f'''Актуальный список учеников
''')
        for student in students:
            print(f'''{student}
            {students_marks[student]}''')


    elif command == 9:
        print('9. Выход из программы')
        break