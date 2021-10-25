import pandas  #pip install pandas #xldr
#pip install openpyxl

import os

path = os.getcwd()

name = "2ИС3" #сделать импорт группы из main

df = pandas.read_excel(path+"\\25-10.xlsx", sheet_name="Корпус 1", engine="openpyxl")

_list_one = []
_list_one.append(df.columns.tolist())
for item in df.values.tolist():
    _list_one.append(item)


df_Two = pandas.read_excel(path+"\\25-10.xlsx", sheet_name="Корпус 2", engine="openpyxl")

_list_two = []
_list_two.append(df_Two.columns.tolist())
for item in df_Two.values.tolist():
    _list_two.append(item)


def parse_for_group(name,_list):
    _returned_list = []
    for _str in _list:
        if name in _str:
            _returned_list.append([name])
            number_of_str = _list.index(_str)
            number_of_column = _str.index(name)
            for i in range(1,9):
                _returned_list.append(_list[number_of_str+i][number_of_column:number_of_column+3])
    return _returned_list

while True:
    print()
    frame = int(input("Введите номер корпуса: "))
    if frame == 1:
        group = str(input("Введите номер группы: ")).upper()
        a = parse_for_group(group,_list_one)
        for j in a:
            print(j)
    else:
        group = str(input("Введите номер группы: ")).upper()
        a = parse_for_group(group,_list_two)
        for j in a:
            print(j)
