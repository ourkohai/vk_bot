import vk_api
import time
import json
import sqlite3

from random import gammavariate, randint as random

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
menu = ['Профиль', 'Расписание']

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
kb_menu = {
    "one_time": False,
    "buttons": [
    [get_button(label=menu[0], color="primary"), get_button(label=menu[1], color="primary")]
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
kb_menu = str(json.dumps(kb_menu, ensure_ascii=False))

_cache_dict = {}
#   //status auth//
# 0 - role
# 1 - building
# 2 - course
# 3 - group
# 4 - auth
#   //role//
# 0 - prepod
# 1 - student

con = sqlite3.connect ("vk_bot.db")
cur = con.cursor()
#cur.execute ("CREATE TABLE user_data (id, role, name, status)")
#sql = "DELETE FROM user_data"
#sql = "UPDATE anal_deboshir SET price = 8860 WHERE name = 'AlenkinaSperm with a mango'"
#cur.execute (sql)
#con.commit()
#cur.execute ("SELECT * FROM user_data")
#p = cur.fetchall()
#print (p)


con = sqlite3.connect ("vk_bot.db")
cur = con.cursor()
#sql = "INSERT INTO user_data VALUES (1,1,1,1)"
#cur.execute (sql)
#cur.execute("DELETE FROM user_data WHERE status = 5")
#con.commit()
cur.execute ("SELECT * FROM user_data")

p = cur.fetchall()
print ("do zikla", p)



while True:
    try:   
        message = vk.method("messages.getConversations", {"offset": 0, "count": 1,"filter": "unanswered"})
        id = message["items"][0]["last_message"]["from_id"]
        text = message["items"][0]["last_message"]["text"]
        info = vk.method("users.get", {"user_ids": id})
        first_name = info[0]['first_name']
        last_name = info[0]['last_name']
        name = first_name + " " + last_name
        print (info)
        print (name)
        print(_cache_dict)
        try:
            cur.execute ("SELECT * FROM user_data WHERE id = {}".format(id))
            user = cur.fetchall()
            print ("aboba", user)
            dan = user[0]
            print ('prod',dan)
            us_id = dan [0]
            us_role = dan [1]
            us_name = dan [2]
            us_status = dan [3]
            _cache_dict = {int("{}".format(id)):[us_id, us_role, us_name, us_status]}
            print(_cache_dict)
        except:
            pass
        if id not in _cache_dict:
            _cache_dict[id] = [id,0,"",-1] #[id, role, name, status]
            _cache_dict[id][2] = name

        print(id,text)
        if _cache_dict[id][3] == -1: #0 - role
            if text not in role:
                msg = "Здравствуйте, для начала необходимо пройти небольшую регистрацию, выберите вашу Роль, нажав кнопку"
                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_role})
            else:
                if text == kb_role[0]:
                    _cache_dict[id][3] = 1
                    _cache_dict[id][1] = 0
                    print (_cache_dict)
                else:
                    _cache_dict[id][3] = 1
                    _cache_dict[id][1] = 1
                    print (_cache_dict)
        elif _cache_dict[id][3] == 1: #1 - building
            if text not in building:
                msg = "Выберите ваш корпус"
                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_building})
            else:
                    building_select = text
                    _cache_dict[id][3] = 2
                    print (_cache_dict)
        elif _cache_dict[id][3] == 2: #2 - course
            if text not in course:
                msg = "Выберите ваш курс"
                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_course})
            else:
                course_select = text
                _cache_dict[id][3] = 3
                print (_cache_dict)
        elif _cache_dict [id][3] == 3: #3 - group
            print(course_select)
            print(building_select)
            if building_select == "Корпус 1":
                if course_select == "1":
                    if text not in group_one_one:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_one})
                    else:
                        _cache_dict[id][3] = 4
                        print (_cache_dict)
                elif course_select == "2":
                    if text not in group_one_two:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_two})
                    else:
                        _cache_dict[id][3] = 4
                        print (_cache_dict)
                elif course_select == "3":
                    if text not in group_one_three:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_three})
                    else:
                        _cache_dict[id][3] = 4
                        print (_cache_dict)
                elif course_select == "4":
                    if text not in group_one_four:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_four})
                    else:
                        _cache_dict[id][3] = 4
                        print (_cache_dict)
            else:
                if course_select == "1":
                    if text not in group_two_one:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_one})
                    else:
                        _cache_dict[id][3] = 4
                        print (_cache_dict)
                elif course_select == "2":
                    if text not in group_two_two:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_two})
                    else:
                        _cache_dict[id][3] = 4
                        print (_cache_dict)
                elif course_select == "3":
                    if text not in group_two_three:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_three})
                    else:
                        _cache_dict[id][3] = 4
                        print (_cache_dict)
                elif course_select == "4":
                    if text not in group_two_four:
                        msg = "Выберите вашу группу"
                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_two_four})
                    else:
                        _cache_dict[id][3] = 4
                        print (_cache_dict)
        elif _cache_dict[id][3] == 4: #запись в бд
            msg = "Записываю ваши данные..."
            vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu})
            _cache_dict[id][3] = 5
            user_info ={"{}".format(id):_cache_dict[id]}
            user_id = str(id)
            a = user_info[user_id]
            cur.execute("INSERT INTO user_data VALUES (?,?,?,?)", a)
            con.commit()
        elif _cache_dict[id][3] == 5:
            if text not in menu:
                msg = "говно с грибами"
                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_menu})
            elif text == "Профиль":
                msg = "{}\n{}\n{}\n{}\n".format(_cache_dict[id][0],_cache_dict[id][1],_cache_dict[id][2],_cache_dict[id][3])
#                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg})

            







#            print (sql)
#            cur.execute(sql)
#            con.commit()

#        if _cache_dict[id][3] == 0: #start 0
#            if text not in role: #bred
#                msg = "Здравствуйте, для начала необходимо пройти небольшую регистрацию, выберите вашу Роль, нажав кнопку"
#                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_role})
#            else: #verno iznachalno, next 1
#                if text == role[0]: #prepod
#                    vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": "error", "keyboard": kb_role})
#                else: #student
#                   if text not in role: #bred
#                        msg = "Здравствуйте, для начала необходимо пройти небольшую регистрацию, выберите вашу Роль, нажав кнопку"
#                        vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_role})
#                    else: #verno iznachalno, next 1
#                        ggb
#        elif _cache_dict[id][3] == 1:
#            print (text)
#            if text == 1:
#                msg = "Выберите вашу группу"
#                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_one})
#            elif text == 2:
#                msg = "Выберите вашу группу"
#                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_two})
#            elif text == 3:
#                msg = "Выберите вашу группу"
#                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_three})
#            elif text == 4:
#                msg = "Выберите вашу группу"
#                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg, "keyboard": kb_group_one_four})
#        elif _cache_dict[id][3] == 2:
#            if text.upper() in group_one_one or text.upper() in group_one_two or text.upper() in group_one_three or text.upper() in group_one_four:
#                msg = "Вы успешно прошли регистрацию."
#                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg})
#                _cache_dict[id][3] = 2
#                _cache_dict[id][2] = text.upper()
#                # подключение к бд и добавление записи
#                # sql.execute("INSERT INTO ............")
#            else:
#                msg = "Вы неверно указали номер группы"
#                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg})
#
#        elif _cache_dict[id][3] == 3:
#            if text.title() == "Профиль":
#                msg = "{}\n{}\n{}\n{}\n".format(_cache_dict[id][0],_cache_dict[id][1],_cache_dict[id][2],_cache_dict[id][3])
#                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": msg})
#            else:
#                vk.method("messages.send", {"peer_id": id, "random_id": random(-100, 100),"message": "error"})
#
#
#
#
    except:
        time.sleep(1)
