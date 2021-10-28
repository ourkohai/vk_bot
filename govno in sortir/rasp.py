from parser_excel import parser_excel
from parser_html import check_rasp
def rasp_studen (data, b, group):
    i = 0
    raspis = parser_excel(data, b, group)
    while i < len(raspis):
        i1 = 0
        while i1 < len(raspis[i]):
            a = raspis[i][i1]
            b = str(a)
            if b == "nan":
               raspis[i][i1] = ""
               i1 += 1
            else:
                i1 += 1
        i += 1
    name = raspis [0]
    one = raspis [2]
    three = raspis [3]
    five = raspis [4]
    six = raspis [5]
    eight = raspis [6]
    ten = raspis [7]
    eleven = raspis [8]
    name_rasp = str(name[0])
    one_rasp = str(one[0]) + " | " + str(one[1]) + " | " + str(one[2])
    three_rasp = str(three[0]) + " | " + str(three[1]) + " | " + str(three[2])
    five_rasp = str(five[0]) + " | " + str(five[1]) + " | " + str(five[2])
    six_rasp = str(six[0]) + " | " + str(six[1]) + " | " + str(six[2])
    eight_rasp = str(eight[0]) + " | " + str(eight[1]) + " | " + str(eight[2])
    ten_rasp = str(ten[0]) + " | " + str(ten[1]) + " | " + str(ten[2])
    eleven_rasp = str(eleven[0]) + " | " + str(eleven[1]) + " | " + str(eleven[2])
    rasp_list = []
    rasp_list.append(name_rasp)
    rasp_list.append(one_rasp)
    rasp_list.append(three_rasp)
    rasp_list.append(five_rasp)
    rasp_list.append(six_rasp)
    rasp_list.append(eight_rasp)
    rasp_list.append(ten_rasp)
    rasp_list.append(eleven_rasp)
    i = -1
    while i < len(rasp_list):
        if " |  | " in rasp_list[i]:
            rasp_list.pop(i)
            i += 1
        else:
            i += 1
    i = 0
    msg = ""
    while i < len(rasp_list):
        msg = msg + "{}\n".format(rasp_list[i])
        i += 1 
    return msg