import re
import csv


def read_csv():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def format_number(contacts_list: list):
    phone_pattern = r'(\+7|8).*?(\d{3}).*?(\d{3}).*?\-*(\d{2}).*?\-*(\d{2})(\s*\(*(доб\.)\s*(\d{4})|)\)?'
    pattern_edit = r'\1(\2)\3-\4-\5 \7\8'

    card_list = []

    for i in contacts_list:
        number_join = ','.join(i)
        formatted_number = re.sub(phone_pattern, pattern_edit, str(number_join))
        number_split = formatted_number.split(',')
        card_list.append(number_split)
    return card_list


def fio(contacts_list):
    name_pattern = r'^([А-ЯЁёа-я]+)(\s*)(\,?)([А-ЯЁёа-я]+)(\s*)(\,?)([А-ЯЁёа-я]*)(\,?)(\,?)(\,?)'
    pattern_edit = r'\1\3\10\4\6\9\7\8'

    change_fio = []

    for i in contacts_list:
        cont_str = ','.join(i)
        formatted_fio = re.sub(name_pattern, pattern_edit, cont_str)
        cont_str = formatted_fio.split(',')
        change_fio.append(cont_str)
    return change_fio


def processing(contacts_list):

    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
    contacts_list_up = list()
    for cont in contacts_list:
        if cont not in contacts_list_up and len(cont) == 7:
            contacts_list_up.append(cont)
    print(contacts_list_up)
    return contacts_list_up


def write_csv(contacts_list):
    with open("phonebook.csv", "w", encoding='utf8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


if __name__ == '__main__':

    contact = read_csv()
    contact = format_number(contact)
    contact = fio(contact)
    contact = processing(contact)
    write_csv(contact)
