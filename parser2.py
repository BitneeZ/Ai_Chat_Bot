import requests
from bs4 import BeautifulSoup
from lxml import html

response = requests.get("https://roslib.rudn.ru/public/uploads/admin/library/books/5df898dfb3951/html/index.html#TOC_id4593586")
html_code = response.text
print(html_code)


#
# import time
#
#
# from selenium import webdriver
#
# # Инициализация веб-драйвера
# driver = webdriver.Chrome()
#
# # Переход на страницу
# driver.get('https://gufo.me/dict/ozhegov?page=1&letter=а')
# time.sleep(5)
# last_height = driver.execute_script("return document.body.scrollHeight")
#
# # Имитация прокрутки вниз (можно изменить в зависимости от сайта)
# while True:
#     # Прокрутка вниз
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Ожидание загрузки контента
#     time.sleep(2)  # Увеличьте время, если контент загружается медленно
#
#     # Проверка новой высоты страницы
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#
#
# html_code = driver.page_source
# driver.quit()
# #BeatiufulSoup
# soup = BeautifulSoup(html_code, 'html.parser')
# movies = soup.find_all('div', class_="word-list")
#
#
# for movie in movies:
#     print(movie.text)
#


# #xtml
# tree = html.fromstring(html_code)
# movie_titles = tree.xpath('//p[@class="text-nowrap overflow-hidden p1-regular"]/text()')
#
# print("Фильмы:", *movie_titles)

