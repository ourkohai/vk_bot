import vk_api
import time
import json
import sqlite3

from rasp import rasp_studen, rasp_prepod
from parser_html import check_rasp
from translate import Translator
from random import randint as random

from Biba import t


vk = vk_api.VkApi(token=t)
vk._auth_token()

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

def rasp_mine_group (data_select): 
    if _cache_dict[id][5] == "Корпус 1":
        b = 1
    else:
        b = 2
    msg = rasp_studen(data_select, b, _cache_dict[id][4])
    if _cache_dict[id][6] == 1:
        if _cache_dict[id][1] == 1:
            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_admin_stud})
        else:
            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_admin_prepod})
    else:
        if _cache_dict[id][1] == 1:
            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_stud})
        else:
            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_prepod})
    
con = sqlite3.connect ("vk_bot.db")
cur = con.cursor()
cur.execute ("SELECT * FROM user_data")
p = cur.fetchall()

data = []
check_rasp()
cur.execute("SELECT * FROM meta_data_excel")
check_output = cur.fetchall()
for i in range (len(check_output)):
    data.append(str(check_output[i][0]))

kb_data = {
    "one_time": True,
    "buttons": []
}
but1 = []
but2 = []
but = kb_data["buttons"]
for i in range (len(data)):
    if len(but1) <= 4:
        but1.append(get_button(label="{}".format(data[i]), color="primary"))
        but = [but1]
    else:
        but2.append(get_button(label="{}".format(data[i]), color="primary"))
        but = [but1, but2]
    kb_data["buttons"] = but

role = ['Преподаватель','Студент']
building = ['Корпус 1', 'Корпус 2']
course = ['1', '2', '3', '4']
group_one_one = ['1Ф8', '1ИС3', '1ИС6', '1ПД7', '1ПД1', '1ПД16', '1Б2', '1ГД11', "12Б10"]
group_one_two = ['2Ф8', '2ИС3', '2Т1', '2ПД7', '2ООП6', '2ГД11', '2Б2', '23Т10']
group_one_three = ['3Ф8', '3Б2', '3Т1', '3ПД7', '3ГД11', '3ИС3', '3ООП6', '34Т10']
group_one_four = ['4ИС3', '4ООП6', '4Т1', '4ПД7', '4ГД11']
group_two_one = ['1ПСО12', '1ПСО13', '1Р5', '1К4', '12К9', '12ПСО14', '12ПСО15']
group_two_two = ['2ЛОГ4', '2ПСО12', '2ПСО13', '2Р5', '23К9', '23ПСО14', '23ПСО15']
group_two_three = ['3Р5', '3ПСО12', '3ПСО13', '3К4']
group_two_four = ['4ПСО12', '4ПСО13']
menu_stud = ['Профиль', 'Расписание','Своё расписание']
menu_prepod = ['Профиль', 'Расписание']
profile = ['Сбросить свой профиль', 'Назад']
menu_admin_stud = ['Профиль', 'Расписание','Своё расписание', 'Анекдоты']
menu_admin_prepod = ['Профиль', 'Расписание', 'Анекдоты']
raspis_menu = ['Расписание по группам', 'Расписание по преподавателям', 'Назад']

kb_role = {
    "one_time": True,
    "buttons": [
    [get_button(label=role[0], color="primary")],
    [get_button(label=role[1], color="primary")]
    ]}
kb_building = {
    "one_time": True,
    "buttons": [
    [get_button(label=building[0], color="primary")],
    [get_button(label=building[1], color="primary")]
    ]}
kb_course = {
    "one_time": True,
    "buttons": [
    [get_button(label=course[0], color="primary"), get_button(label=course[1], color="primary"), get_button(label=course[2], color="primary"), get_button(label=course[3], color="primary")],
    ]}
kb_group_one_one = {
    "one_time": True,
    "buttons": [
    [get_button(label=group_one_one[0], color="primary"), get_button(label=group_one_one[1], color="primary"), get_button(label=group_one_one[2], color="primary"), get_button(label=group_one_one[3], color="primary")],
    [get_button(label=group_one_one[4], color="primary"), get_button(label=group_one_one[5], color="primary"), get_button(label=group_one_one[6], color="primary"), get_button(label=group_one_one[7], color="primary")],
    [get_button(label=group_one_one[8], color="primary")]
    ]}
kb_group_one_two = {
    "one_time": True,
    "buttons": [
    [get_button(label=group_one_two[0], color="primary"), get_button(label=group_one_two[1], color="primary"), get_button(label=group_one_two[2], color="primary"), get_button(label=group_one_two[3], color="primary")],
    [get_button(label=group_one_two[4], color="primary"), get_button(label=group_one_two[5], color="primary"), get_button(label=group_one_two[6], color="primary"), get_button(label=group_one_two[7], color="primary")]
    ]}
kb_group_one_three = {
    "one_time": True,
    "buttons": [
    [get_button(label=group_one_three[0], color="primary"), get_button(label=group_one_three[1], color="primary"), get_button(label=group_one_three[2], color="primary"), get_button(label=group_one_three[3], color="primary")],
    [get_button(label=group_one_three[4], color="primary"), get_button(label=group_one_three[5], color="primary"), get_button(label=group_one_three[6], color="primary"), get_button(label=group_one_three[7], color="primary")]
    ]}
kb_group_one_four = {
    "one_time": True,
    "buttons": [
    [get_button(label=group_one_four[0], color="primary"), get_button(label=group_one_four[1], color="primary"), get_button(label=group_one_four[2], color="primary"), get_button(label=group_one_four[3], color="primary")],
    [get_button(label=group_one_four[4], color="primary")]
    ]}
kb_group_two_one = {
    "one_time": True,
    "buttons": [
    [get_button(label=group_two_one[0], color="primary"), get_button(label=group_two_one[1], color="primary"), get_button(label=group_two_one[2], color="primary"), get_button(label=group_two_one[3], color="primary")],
    [get_button(label=group_two_one[4], color="primary"), get_button(label=group_two_one[5], color="primary"), get_button(label=group_two_one[6], color="primary")]
    ]}
kb_group_two_two = {
    "one_time": True,
    "buttons": [
    [get_button(label=group_two_two[0], color="primary"), get_button(label=group_two_two[1], color="primary"), get_button(label=group_two_two[2], color="primary"), get_button(label=group_two_two[3], color="primary")],
    [get_button(label=group_two_two[4], color="primary"), get_button(label=group_two_two[5], color="primary"), get_button(label=group_two_two[6], color="primary")]
    ]}
kb_group_two_three = {
    "one_time": True,
    "buttons": [
    [get_button(label=group_two_three[0], color="primary"), get_button(label=group_two_three[1], color="primary"), get_button(label=group_two_three[2], color="primary"), get_button(label=group_two_three[3], color="primary")]
    ]}
kb_group_two_four = {
    "one_time": True,
    "buttons": [
    [get_button(label=group_two_four[0], color="primary"), get_button(label=group_two_four[1], color="primary")]
    ]}
kb_menu_stud = {
    "one_time": False,
    "buttons": [
    [get_button(label=menu_stud[0], color="primary"), get_button(label=menu_stud[1], color="primary")],
    [get_button(label=menu_stud[2], color="primary")]
    ]}
kb_menu_prepod = {
    "one_time": False,
    "buttons": [
    [get_button(label=menu_prepod[0], color="primary"), get_button(label=menu_prepod[1], color="primary")]
    ]}
kb_profile = {
    "one_time": True,
    "buttons": [
    [get_button(label=profile[0], color="primary"), get_button(label=profile[1], color="primary")]
    ]}
kb_menu_admin_stud = {
    "one_time": False,
    "buttons": [
    [get_button(label=menu_admin_stud[0], color="primary"), get_button(label=menu_admin_stud[3], color="primary")],
    [get_button(label=menu_admin_stud[1], color="primary"), get_button(label=menu_admin_stud[2], color="primary")]
    ]}
kb_menu_admin_prepod = {
    "one_time": False,
    "buttons": [
    [get_button(label=menu_admin_prepod[0], color="primary"), get_button(label=menu_admin_prepod[2], color="primary")],
    [get_button(label=menu_admin_prepod[1], color="primary")]
    ]}
kb_raspis_menu = {
    "one_time": False,
    "buttons": [
    [get_button(label=raspis_menu[0], color="primary"), get_button(label=raspis_menu[2], color="negative")],
    [get_button(label=raspis_menu[1], color="primary")]
    ]}

kb_role = str(json.dumps(kb_role, ensure_ascii=False))
kb_course = str(json.dumps(kb_course, ensure_ascii=False))
kb_building = str(json.dumps(kb_building, ensure_ascii=False))
kb_group_one_one = str(json.dumps(kb_group_one_one, ensure_ascii=False))
kb_group_one_two = str(json.dumps(kb_group_one_two, ensure_ascii=False))
kb_group_one_three = str(json.dumps(kb_group_one_three, ensure_ascii=False))
kb_group_one_four = str(json.dumps(kb_group_one_four, ensure_ascii=False))
kb_group_two_one = str(json.dumps(kb_group_two_one, ensure_ascii=False))
kb_group_two_two = str(json.dumps(kb_group_two_two, ensure_ascii=False))
kb_group_two_three = str(json.dumps(kb_group_two_three, ensure_ascii=False))
kb_group_two_four = str(json.dumps(kb_group_two_four, ensure_ascii=False))
kb_menu_stud = str(json.dumps(kb_menu_stud, ensure_ascii=False))
kb_menu_prepod = str(json.dumps(kb_menu_prepod, ensure_ascii=False))
kb_menu_admin_stud = str(json.dumps(kb_menu_admin_stud, ensure_ascii=False))
kb_menu_admin_prepod = str(json.dumps(kb_menu_admin_prepod, ensure_ascii=False))
kb_data = str(json.dumps(kb_data, ensure_ascii=False))
kb_profile = str(json.dumps(kb_profile, ensure_ascii=False))
kb_raspis_menu = str(json.dumps(kb_raspis_menu, ensure_ascii=False))

_cache_dict = {} 
#[id, role, name, status, group, building]
#   //status auth//
# -1 - new user
# 0 - role
# 1 - building
# 2 - course
# 3 - group
# 4 - isnert bd
# 5 - auth
#   //role//
# 0 - prepod
# 1 - student

admin_list = [177157427, 501057196, 123537807]
text_list = []
data_select = 0
course_select = 0
rasp_building = 0
rasp_group = 0
profile_select = 0
raspis_switch = 0
main_raspis_switch = 0
profile_switch = 0
raspis_prepod_switch = 0
raspis_menu_switch = 0
anek_list = []

while True:
    try:  
        message = vk.method("messages.getConversations", {"offset": 0, "count": 1,"filter": "unanswered"})
        id = message["items"][0]["last_message"]["from_id"]
        text = message["items"][0]["last_message"]["text"]
        try:
            cur.execute ("SELECT * FROM user_data WHERE id = {}".format(id))
            user = cur.fetchall()[0]
            _cache_dict = {int("{}".format(id)):[user[0], user[1], user[2], user[3], user[4], user[5], user[6]]}
        except:
            pass
        if id not in _cache_dict:
                _cache_dict[id] = [id,0,"",-1,"","", 0] #[id, role, name, status, group, building, admin]
                info = vk.method("users.get", {"user_ids": id})
                first_name = info[0]['first_name']
                last_name = info[0]['last_name']
                name = first_name + " " + last_name
                translator = Translator(to_lang="Russian")
                name = translator.translate(name)
                _cache_dict[id][2] = name
        print(_cache_dict[id][2], "|", text)
        if raspis_menu_switch == 1:
                if text not in raspis_menu:
                    msg = "Выберите тип расписания"
                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_raspis_menu})
                else:
                    if text == "Расписание по группам":
                        raspis_menu_switch = 2
                        raspis_switch = 1
                        text_list.append(text)
                    elif text == "Назад":
                        raspis_menu_switch = 0
                    else:
                        raspis_menu_switch = 2
                        raspis_prepod_switch = 1
                        text_list.append(text)
        elif raspis_menu_switch == 2:
            if raspis_switch == 1:
                if "Расписание по группам" in text_list:
                    if text not in data:
                        msg = "Выберите дату"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_data})
                    else:
                        data_select = text
                        text_list.clear()
                        text_list.append(text)
                elif data_select in text_list:
                    if text not in building:
                        msg = "Выберите нужный корпус"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_building})
                    else:
                        rasp_building = text
                        text_list.clear() 
                        text_list.append(text)
                elif rasp_building in text_list:
                    if text not in course:
                        msg = "Выберите нужный курс"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_course})
                    else:
                        course_select = text
                        text_list.clear() 
                        text_list.append(text)
                elif course_select in text_list:
                    if rasp_building == "Корпус 1":
                        if course_select == "1":
                            if text not in group_one_one:
                                msg = "Выберите нужную группу"
                                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_one})
                            else:
                                rasp_group = text
                                text_list.clear() 
                                text_list.append(text)
                        elif course_select == "2":
                            if text not in group_one_two:
                                msg = "Выберите нужную группу"
                                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_two})
                            else:
                                rasp_group = text
                                text_list.clear() 
                                text_list.append(text)
                        elif course_select == "3":
                            if text not in group_one_three:
                                msg = "Выберите нужную группу"
                                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_three})
                            else:
                                rasp_group = text
                                text_list.clear() 
                                text_list.append(text)
                        elif course_select == "4":
                            if text not in group_one_four:
                                msg = "Выберите нужную группу"
                                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_four})
                            else:
                                rasp_group = text
                                text_list.clear() 
                                text_list.append(text)
                    else:
                        if course_select == "1":
                            if text not in group_two_one:
                                msg = "Выберите нужную группу"
                                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_one})
                            else:
                                rasp_group = text
                                text_list.clear() 
                                text_list.append(text)
                        elif course_select == "2":
                            if text not in group_two_two:
                                msg = "Выберите нужную группу"
                                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_two})
                            else:
                                rasp_group = text
                                text_list.clear() 
                                text_list.append(text)
                        elif course_select == "3":
                            if text not in group_two_three:
                                msg = "Выберите нужную группу"
                                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_three})
                            else:
                                rasp_group = text
                                text_list.clear() 
                                text_list.append(text)
                        elif course_select == "4":
                            if text not in group_two_four:
                                msg = "Выберите нужную группу"
                                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_four})
                            else:
                                rasp_group = text
                                text_list.clear() 
                                text_list.append(text)
                elif rasp_group in text_list:
                    if rasp_building == "Корпус 1":
                        b = 1
                    else:
                        b = 2
                    msg = rasp_studen(data_select, b, rasp_group)
                    if _cache_dict[id][6] == 1:
                        if _cache_dict[id][1] == 1:
                            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_admin_stud})
                        else:
                            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_admin_prepod})
                    else:
                        if _cache_dict[id][1] == 1:
                            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_stud})
                        else:
                            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_prepod})
                    raspis_switch = 0
                    raspis_menu_switch = 0
                    text_list.clear()
            elif raspis_prepod_switch == 1:
                if "Расписание по преподавателям" in text_list:
                    if text not in data:
                        msg = "Выберите дату"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_data})
                    else:
                        data_select_prepod = text
                        text_list.clear()
                        text_list.append(data_select_prepod)
                elif data_select_prepod in text_list:
                    if text in text_list:
                        msg = "Введите фамилию преподавателя"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg})
                    else:
                        name = text.capitalize()
                        msg = rasp_prepod(data_select_prepod, name)
                        if msg != "":
                            if _cache_dict[id][6] == 1:
                                if _cache_dict[id][1] == 1:
                                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_admin_stud})
                                else:
                                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_admin_prepod})
                            else:
                                if _cache_dict[id][1] == 1:
                                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_stud})
                                else:
                                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_prepod})
                        else:
                            msg = "У этого преподавателя в выбранный день пары отсутствуют"
                            if _cache_dict[id][6] == 1:
                                if _cache_dict[id][1] == 1:
                                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_admin_stud})
                                else:
                                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_admin_prepod})
                            else:
                                if _cache_dict[id][1] == 1:
                                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_stud})
                                else:
                                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_prepod})
                        text_list.clear()
                        raspis_prepod_switch = 0
                        raspis_menu_switch = 0
        elif main_raspis_switch == 1:
            if "Своё расписание" in text_list:
                if text not in data:
                    msg = "Выберите дату"
                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_data})
                else:
                    rasp_mine_group(text)
                    text_list.clear()
                    main_raspis_switch = 0
        elif profile_switch == 1:
            if "Профиль" in text_list:
                if text not in profile:
                    if _cache_dict[id][1] == 1:
                        r = "Студент"
                    else:
                        r = "Преподаватель"
                    if _cache_dict[id][6] == 0:
                        status = "Авторизованный"
                    else:
                        status = "Авторизованный | Админ"
                    msg = "Ваш профиль\n{}\nВаша роль: {} {} {}\n{}\n".format(_cache_dict[id][2],r,_cache_dict[id][4],_cache_dict[id][5],status)
                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_profile})
                else:
                    profile_select = text
                    text_list.clear()
                    text_list.append(text)
            elif profile_select in text_list:
                if profile_select == "Сбросить свой профиль":
                        _cache_dict[id] = [id,0,"",-1,"","", 0]
                        info = vk.method("users.get", {"user_ids": id})
                        first_name = info[0]['first_name']
                        last_name = info[0]['last_name']
                        name = first_name + " " + last_name
                        translator = Translator(to_lang="Russian")
                        name = translator.translate(name)
                        _cache_dict[id][2] = name
                        text_list.clear()
                        cur.execute("DELETE FROM user_data WHERE id = {}".format(id))
                        profile_switch = 0
                else:
                    profile_switch = 0
                    text_list.clear()
        elif _cache_dict[id][3] == 5:
            if _cache_dict[id][6] == 1:
                if _cache_dict[id][1] == 1:
                    if text not in menu_admin_stud:
                        msg = "говно с грибами"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100), "message": msg, "keyboard": kb_menu_admin_stud})
                    else:
                        if text == "Профиль":
                            profile_switch = 1
                            text_list.clear()
                            text_list.append(text)
                        elif text == "Своё расписание":
                            main_raspis_switch = 1
                            text_list.clear()
                            text_list.append(text) 
                        elif text == "Расписание":
                            raspis_menu_switch = 1
                            text_list.clear()
                        elif text == "Анекдоты":
                            perebor = 0
                            cur.execute ("SELECT * FROM aneki")
                            p = cur.fetchall()
                            i1 = 0
                            i = random (0, (len(p)-1))
                            while i in anek_list:
                                i = random (0, (len(p)-1))
                                perebor += 1
                            if perebor > 12:
                                anek_list.clear()
                            else:
                                anek_list.append(i)
                            msg = ""
                            while i1 < len(p[i]):
                                anek_str = p[i][i1]
                                if anek_str == "":
                                    i1 += 1 
                                else:
                                    msg = msg + "{}\n".format(anek_str)
                                    i1 += 1
                            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg})
                else:
                    if text not in menu_admin_prepod:
                        msg = "говно с грибами"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100), "message": msg, "keyboard": kb_menu_admin_prepod})
                    else:
                        if text == "Профиль":
                            profile_switch = 1
                            text_list.clear()
                            text_list.append(text)
                        elif text == "Расписание":
                            raspis_menu_switch = 1
                            text_list.clear()
                        elif text == "Анекдоты":
                            perebor = 0
                            cur.execute ("SELECT * FROM aneki")
                            p = cur.fetchall()
                            i1 = 0
                            i = random (0, (len(p)-1))
                            while i in anek_list:
                                i = random (0, (len(p)-1))
                                perebor += 1
                            if perebor > 12:
                                anek_list.clear()
                            else:
                                anek_list.append(i)
                            msg = ""
                            while i1 < len(p[i]):
                                anek_str = p[i][i1]
                                if anek_str == "":
                                    i1 += 1 
                                else:
                                    msg = msg + "{}\n".format(anek_str)
                                    i1 += 1
                            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg})
            else:
                if _cache_dict[id][1] == 1:
                    if text not in menu_stud:
                        msg = "Главное меню"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100), "message": msg,"keyboard": kb_menu_stud})
                    else:
                        if text == "Профиль":
                            profile_switch = 1
                            text_list.clear()
                            text_list.append(text)
                        elif text == "Своё расписание":
                            main_raspis_switch = 1
                            text_list.clear()
                            text_list.append(text) 
                        elif text == "Расписание":
                            raspis_menu_switch = 1
                            text_list.clear()
                else:
                    if text not in menu_prepod:
                        msg = "Главное меню"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100), "message": msg,"keyboard": kb_menu_prepod})
                    else:
                        if text == "Профиль":
                            profile_switch = 1
                            text_list.clear()
                            text_list.append(text)
                        elif text == "Расписание":
                            raspis_menu_switch = 1
                            text_list.clear()
        if _cache_dict[id][3] == -1: #-1 - role
            if text not in role:
                msg = "Здравствуйте, для начала необходимо пройти небольшую регистрацию, выберите вашу роль, нажав кнопку"
                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_role})
            else:
                if text == "Преподаватель":
                    _cache_dict[id][3] = 4
                    _cache_dict[id][1] = 0
                else:
                    _cache_dict[id][3] = 1
                    _cache_dict[id][1] = 1
        elif _cache_dict[id][3] == 1: #1 - building
            if text not in building:
                msg = "Выберите ваш корпус"
                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_building})
            else:
                    _cache_dict[id][5] = text
                    _cache_dict[id][3] = 2
        elif _cache_dict[id][3] == 2: #2 - course
            if text not in course:
                msg = "Выберите ваш курс"
                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_course})
            else:
                course_select = text
                _cache_dict[id][3] = 3
        elif _cache_dict [id][3] == 3: #3 - group
            if _cache_dict[id][5] == "Корпус 1":
                if course_select == "1":
                    if text not in group_one_one:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_one})
                    else:
                        _cache_dict[id][4] = text
                        _cache_dict[id][3] = 4
                elif course_select == "2":
                    if text not in group_one_two:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_two})
                    else:
                        _cache_dict[id][4] = text
                        _cache_dict[id][3] = 4
                elif course_select == "3":
                    if text not in group_one_three:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_three})
                    else:
                        _cache_dict[id][4] = text
                        _cache_dict[id][3] = 4
                elif course_select == "4":
                    if text not in group_one_four:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_four})
                    else:
                        _cache_dict[id][4] = text
                        _cache_dict[id][3] = 4
            else:
                if course_select == "1":
                    if text not in group_two_one:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_one})
                    else:
                        _cache_dict[id][4] = text
                        _cache_dict[id][3] = 4
                elif course_select == "2":
                    if text not in group_two_two:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_two})
                    else:
                        _cache_dict[id][4] = text
                        _cache_dict[id][3] = 4
                elif course_select == "3":
                    if text not in group_two_three:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_three})
                    else:
                        _cache_dict[id][4] = text
                        _cache_dict[id][3] = 4
                elif course_select == "4":
                    if text not in group_two_four:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_four})
                    else:
                        _cache_dict[id][4] = text
                        _cache_dict[id][3] = 4
        elif _cache_dict[id][3] == 4: #запись в бд
            msg = "Записываю ваши данные..."
            if int(id) in admin_list:
                _cache_dict[id][6] = 1
            if _cache_dict[id][6] == 0:
                if _cache_dict[id][1] == 1:
                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_stud})
                else:
                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_prepod})
            else:
                if _cache_dict[id][1] == 1:
                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_admin_stud})
                else:
                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu_admin_prepod})
                pass
            user_info ={"{}".format(id):_cache_dict[id]}
            user_id = str(id)
            a = user_info[user_id]
            _cache_dict[id][3] = 5
            cur.execute("INSERT INTO user_data VALUES (?,?,?,?,?,?,?)", a)
            con.commit()        
    except:
        time.sleep(1)
