groupmates = [
    {
        "name":"Александр",
        "surname":"Иванов",
        "exams":['Информатика','ЭЭиС','Web'],
        "marks":[4,3,5]
    },
    {
        "name":"Иван",
        "surname":"Петров",
        "exams":['Историю','АиГ','КТП'],
        "marks":[4,5,4]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ['Историю', 'АиГ', 'КТП'],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ['филососфия', 'ИС', 'КТП'],
        "marks": [5, 5, 5]
    }
]

n = int(input('Выберите минимальный балл , от которого хотите отфильтровать: '))


def print_students(students):

    print ("name".ljust(13), "surname".ljust(15), "exams".ljust(23), "marks".ljust(20))
    for student in students:
        print (student["name"].ljust(13), student["surname"].ljust(8), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
    print("Нужный студент(ы)↓")
    return [x for x in filter(lambda x: sum(x.get("marks"))/len(x.get("marks")) > n, groupmates)]
print(print_students(groupmates))


