import requests as req
import sqlite3
import os

from bs4 import BeautifulSoup #pip install lxml
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
    site_parse = parser_html()
    cur.execute ("SELECT * FROM meta_data_excel")
    meta_data_excel = cur.fetchall()
    meta_data = list(site_parse.items())
    if len(meta_data_excel) == len(meta_data): #если скач = дост  |   проверка актуальности
        for i in range(len(meta_data)):
            name_bd = meta_data_excel[i][0]
            data_bd = meta_data_excel[i][1]
            if site_parse[name_bd] == data_bd: #проверка актуальности
                pass
            else:
                cur.execute("UPDATE meta_data_excel SET data = '{}' WHERE name = '{}'".format(meta_data[i][1], name_bd)) #обновлям данные в бд
                con.commit()
                file_path = path + "\\{}.xlsx".format(meta_data[i][0]) #удаляем старый файл
                os.remove(file_path)
                url = "https://a.nttek.ru/xlsx/{}.xlsx".format(meta_data[i][0]) #скачиваем новый
                r = req.get(url)
                with open('{}.xlsx'.format(meta_data[i][0]), 'wb') as outfile:
                    outfile.write(r.content)
    elif len(meta_data_excel) > len(meta_data): #если скач > дост |   проверка актуальности, удаление старых файлов
        for i in range(len(meta_data_excel)):
            try:
                name_bd = meta_data_excel[i][0]
                data_bd = meta_data_excel[i][1]
                if site_parse[name_bd] == data_bd:
                    pass
                else:
                    cur.execute("UPDATE meta_data_excel SET data = '{}' WHERE name = '{}'".format(site_parse[name_bd], name_bd))
                    con.commit()
                    file_path = path + "\\{}.xlsx".format(meta_data_excel[i][0])
                    os.remove(file_path)
                    url = "https://a.nttek.ru/xlsx/{}.xlsx".format(meta_data[i][0])
                    r = req.get(url)
                    with open('{}.xlsx'.format(meta_data[i][0]), 'wb') as outfile:
                        outfile.write(r.content)
            except: # старые файлы
                cur.execute("DELETE FROM meta_data_excel WHERE name = '{}'".format(name_bd))
                con.commit()
                file_path = path + "\\{}.xlsx".format(meta_data_excel[i][0])
                os.remove(file_path)
    elif len(meta_data_excel) < len(meta_data): #если скач < дост |   проверка актуальности, скачивание новых файлов
        for i in range(len(meta_data)):
            try:
                name_bd = meta_data_excel[i][0]
                data_bd = meta_data_excel[i][1]
                if site_parse[name_bd] == data_bd:
                    pass
                else:
                    cur.execute("UPDATE meta_data_excel SET data = {} WHERE name = '{}'".format(site_parse[name_bd], name_bd))
                    con.commit()
                    file_path = path + "\\{}.xlsx".format(meta_data_excel[i][0])
                    os.remove(file_path)
                    url = "https://a.nttek.ru/xlsx/{}.xlsx".format(meta_data[i][0])
                    r = req.get(url)
                    with open('{}.xlsx'.format(meta_data[i][0]), 'wb') as outfile:
                        outfile.write(r.content)
            except: # старые файлы
                file_info = []
                file_info.append(meta_data[i][0]) 
                file_info.append(meta_data[i][1])
                cur.execute("INSERT INTO meta_data_excel VALUES(?,?)", file_info)
                con.commit()
                url = "https://a.nttek.ru/xlsx/{}.xlsx".format(meta_data[i][0])
                r = req.get(url)
                with open('{}.xlsx'.format(meta_data[i][0]), 'wb') as outfile:
                    outfile.write(r.content)