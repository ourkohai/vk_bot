from bs4 import BeautifulSoup #pip install lxml
import requests as req
import sqlite3
import os

from requests.sessions import Request


def parser_html():
    reqOnline = req.get("https://a.nttek.ru/xlsx/")
    onlSoup = BeautifulSoup(reqOnline.content, 'lxml')
    getOnline = onlSoup.find_all('td')
    r = len(getOnline)
    v = r - 2
    rasp_old = getOnline[6:v]
    i = 0
    rasp = []
    while i < len(rasp_old): #оставляем только название и время
        rasp.append(rasp_old[i])
        i = i+1
        rasp.append(rasp_old[i])
        i = i+4
    #i = 0
    #for i in range(len(rasp)):
    #   print(rasp[i])
        
    name = []
    data = []

    for i in range(len(rasp)): #словарь название:дата
        if i%2 != 0:
            rs = str(rasp[i])[18:34]
            data.append(rs)
        else:
            rs = str(rasp[i])[13:18]
            name.append(rs)
    raspisanie = dict(zip(name, data))
    return raspisanie
path = os.getcwd()

con = sqlite3.connect ("vk_bot.db")
cur = con.cursor()
#cur.execute("DELETE FROM meta_data_excel WHERE name ")
#con.commit()
cur.execute("SELECT * FROM meta_data_excel")
p = cur.fetchall()
def check_rasp():
    old_parse = parser_html()
    cur.execute ("SELECT * FROM meta_data_excel")
    meta_data_excel = cur.fetchall() # [('25-10', '2021-10-22 17:22'), ('26-10', '2021-10-25 12:05')]      | bd 
    meta_data = list(old_parse.items()) # [('25-10', '2021-10-22 17:22'), ('26-10', '2021-10-25 12:05')]   | parser
    if len(meta_data_excel) == len(meta_data): #если скач = дост  |   проверка актуальности
        for i in range(len(meta_data)):
            name_bd = meta_data_excel[i][0]
            data_bd = meta_data_excel[i][1]
            if old_parse[name_bd] == data_bd: #проверка актуальности
                pass
            else:
                print(old_parse)
                print(name_bd)
                cur.execute("UPDATE meta_data_excel SET data = {} WHERE name = '{}'".format(old_parse[name_bd], name_bd)) #обновлям данные в бд
                con.commit()
                file_path = path + "\\{}.xlsx".format(meta_data[i][0]) #удаляем старый файл
                os.remove(file_path)
                url = "https://a.nttek.ru/xlsx/{}.xlsx".format(meta_data[i][0]) #скачиваем новый
                r = req.get(url)
                with open('{}.xlsx'.format(meta_data[i][0]), 'wb') as outfile:
                    outfile.write(r.content)
    elif len(meta_data_excel) > len(meta_data): #если скач > дост |   проверка актуальности, удаление старых файлов
        for i in range(len(meta_data_excel)):
            try: #  проверяет доступные файлы на актуальность
                name_bd = meta_data_excel[i][0]
                data_bd = meta_data_excel[i][1]
                if old_parse[name_bd] == data_bd: #проверка актуальности
                    pass
                else:
                    cur.execute("UPDATE meta_data_excel SET data = {} WHERE name = '{}'".format(old_parse[name_bd], name_bd)) #обновлям данные в бд
                    con.commit()
                    file_path = path + "\\{}.xlsx".format(meta_data[i][0]) #удаляем старый файл
                    os.remove(file_path)
                    url = "https://a.nttek.ru/xlsx/{}.xlsx".format(meta_data[i][0]) #скачиваем новый
                    r = req.get(url)
                    with open('{}.xlsx'.format(meta_data[i][0]), 'wb') as outfile:
                        outfile.write(r.content)
            except: # старые файлы
                cur.execute("DELETE FROM meta_data_excel WHERE name = '{}'".format(name_bd[i]))
                con.commit()
                file_path = path + "\\{}.xlsx".format(meta_data[i][0]) #удаляем старый файл
                os.remove(file_path)
    elif len(meta_data_excel) < len(meta_data): #если скач < дост |   проверка актуальности, скачивание новых файлов
        for i in range(len(meta_data)):
            try: #  проверяет доступные файлы на актуальность
                name_bd = meta_data_excel[i][0]
                data_bd = meta_data_excel[i][1]
                if old_parse[name_bd] == data_bd: #проверка актуальности
                    pass
                else:
                    cur.execute("UPDATE meta_data_excel SET data = {} WHERE name = '{}'".format(old_parse[name_bd], name_bd)) #обновлям данные в бд
                    con.commit()
                    file_path = path + "\\{}.xlsx".format(meta_data[i][0]) #удаляем старый файл
                    os.remove(file_path)
                    url = "https://a.nttek.ru/xlsx/{}.xlsx".format(meta_data[i][0]) #скачиваем новый
                    r = req.get(url)
                    with open('{}.xlsx'.format(meta_data[i][0]), 'wb') as outfile:
                        outfile.write(r.content)
            except: # старые файлы
                l = []
                l.append(meta_data[i][0])
                l.append(meta_data[i][1])
                cur.execute("INSERT INTO meta_data_excel VALUES(?,?)", l)
                con.commit()
                url = "https://a.nttek.ru/xlsx/{}.xlsx".format(meta_data[i][0]) #скачиваем новый
                r = req.get(url)
                with open('{}.xlsx'.format(meta_data[i][0]), 'wb') as outfile:
                    outfile.write(r.content)