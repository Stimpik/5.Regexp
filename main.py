from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
phone_book = []
phonebook = {}
pattern = r"(^[А-Я][а-я]+)([,|\s][А-Я][а-я]+)([,|\s][А-Я][а-я]+)?(,{1,3}[А-Яа-я]+)?(,[^,]*)?(,[\+7|8]+)?([\s|(]+)?(\d{3})?([\s|)|-]+)?(\d{3})?([\s|-])?(\d{2})?([\s|-])?(\d{2})?([(|\s]+)?(доб.\s\d{4})?([)|\s]+)?(,[A-Za-z0-9.,@]+)?"
subst = r'\1;\2;\3;\4;\5;+7(\8)\10\12\14 \16;\18'

for line in contacts_list[1:]:
    phone_book.append(re.sub(pattern, subst, ','.join(line)).replace(',', '').split(';'))

for element in phone_book:
    if element[0] not in phonebook:
        d = {element[0]: element[1:]}
        phonebook.update(d)
    else:
        for x in range(len(phonebook[element[0]])):
            if len(phonebook[element[0]][x]) == 0:
                phonebook[element[0]][x] = element[x + 1]

final_book = []
for x, y in phonebook.items():
    temp = []
    temp.append(x)
    for z in y:
        temp.append(z)
    final_book.append(temp)
tag = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
final_book.insert(0, tag)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_book)
