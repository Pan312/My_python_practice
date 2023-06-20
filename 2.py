import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

web_page = requests.get('https://live.skillbox.ru/playlists/code/python/')
soup = BeautifulSoup(web_page.text, 'html.parser')

work_book = Workbook()
work_sheet = work_book.active

items = soup.find_all(class_='playlist-inner__item')

for elem in items:
    title = elem.find(class_="playlist-inner-card__title hover-card__text t t--3").text
    relative_url = elem.find(class_='playlist-inner-card hover-card').attrs['href']
    timing = elem.find(class_='playlist-inner-card__small-info').text.strip().split(',')[-1].strip()
    url = 'https://live.skillbox.ru' + relative_url
    row = [title, url, timing]
    print(row)
    work_sheet.append(row)
    work_book.save('Вебинары про Python от Skillbox.xlsx')
