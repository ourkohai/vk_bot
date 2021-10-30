from parser_excel import parser_excel, parser_excel_prepod
def rasp_studen (data, b, group):
    raspis = parser_excel(data, b, group)
    rasp_list = []
    for i in raspis:
        if len(i) != 1:
            if "nan" not in str(i):
                a = str(i[0]) + " | " + str(i[1]) + " | " + str(i[2])
                rasp_list.append(a)
            else:
                raspis.pop(raspis.index(i))
        else:
            rasp_list.append(str(i[0]))
    i = 0
    msg = ""
    while i < len(rasp_list):
        msg = msg + "{}\n".format(rasp_list[i])
        i += 1 
    return msg

def rasp_prepod(data, name):
    raspis = parser_excel_prepod(data, name)
    rasp_list = []
    for i in raspis:
        a = str(i[0]) + " | " + str(i[1]) + " | " + str(i[2]) + " | " + str(i[3])
        rasp_list.append(a)
    i = 0
    msg = ""
    while i < len(rasp_list):
        msg = msg + "{}\n".format(rasp_list[i])
        i += 1
    return msg