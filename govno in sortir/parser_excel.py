import pandas  #pip install pandas
#pip install openpyxl

import os


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

def parser_excel (data, frame, group):
    path = os.getcwd()
    df = pandas.read_excel(path+"\\{}.xlsx".format(data), sheet_name="Корпус 1", engine="openpyxl")

    _list_one = []
    _list_one.append(df.columns.tolist())
    for item in df.values.tolist():
        _list_one.append(item)


    df_Two = pandas.read_excel(path+"\\{}.xlsx".format(data), sheet_name="Корпус 2", engine="openpyxl")

    _list_two = []
    _list_two.append(df_Two.columns.tolist())
    for item in df_Two.values.tolist():
        _list_two.append(item)

    raspis = []
    if frame == 1:
        a = parse_for_group(group,_list_one)
        for j in a:
                raspis.append(j)
        return raspis
    else:
        a = parse_for_group(group,_list_two)
        for j in a:
            raspis.append(j)
        return raspis
    
def parser_excel_prepod(data, name):
    path = os.getcwd()
    df = pandas.read_excel(path+"\\{}.xlsx".format(data), sheet_name="Корпус 1", engine="openpyxl")

    _list_one = []
    _list_one.append(df.columns.tolist())
    for item in df.values.tolist():
        _list_one.append(item)


    df_Two = pandas.read_excel(path+"\\{}.xlsx".format(data), sheet_name="Корпус 2", engine="openpyxl")

    _list_two = []
    _list_two.append(df_Two.columns.tolist())
    for item in df_Two.values.tolist():
        _list_two.append(item)
    _prepod = []
    for i in _list_two:
        for j in i:
            if name in str(j):
                a = i.index(j)
                b = _list_two.index(i)
                b = b-b%9
                _prepod.append ([_list_two[b][a-1],i[a-1],i[a],i[a+1]])
    for i in _list_one:
        for j in i:
            if name in str(j):
                a = i.index(j)
                b = _list_one.index(i)
                b = b-b%9
                _prepod.append([_list_one[b][a-1],i[a-1],i[a],i[a+1]])
    return _prepod