from bs4 import BeautifulSoup #pip install lxml
import requests as req

def parser_html():
    reqOnline = req.get("https://a.nttek.ru/xlsx/")
    onlSoup = BeautifulSoup(reqOnline.content, 'lxml')
    getOnline = onlSoup.find_all('td')
    r = len(getOnline)
    v = r - 2
    rasp = getOnline[6:v]
    l = len(rasp)
    i = 0
    while i < l: #оставляем только название и время
        c = i+2
        d = c+3
        del rasp [c:d]
        i = d
    print (rasp[0]) #проверяем че вытащили
    print (rasp[1])
    print (rasp[2])
    print (rasp[3])
    i = 0
    name = []
    data = []
    for i in range(len(rasp)): #словарь название:дата
        if i%2 != 0:
            data.append(rasp[i])
        else:
            name.append(rasp[i])
    raspisanie = dict(zip(name, data))
    return raspisanie