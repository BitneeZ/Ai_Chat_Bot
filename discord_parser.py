# import pandas as pd
#
# df = pd.read_csv('chats_mk.csv')
# print(df)
import requests
import json
h = {'authorization': ''} #ENTER KEY HERE
channel_id = 'f'


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Путь к драйверу для вашего браузера (например, ChromeDriver)
driver = webdriver.Chrome()

# Откройте веб-версию Discord
driver.get("https://discord.com/login")

# Дайте пользователю время войти в аккаунт
print("Войдите в аккаунт вручную...")
time.sleep(60)  # Увеличьте время, если требуется

# Перейдите на страницу канала
channel_url = f"https://discord.com/channels/{channel_id}"
driver.get(channel_url)
time.sleep(5)

# Получите сообщения
messages = driver.find_elements(By.CLASS_NAME, "message")  # Класс сообщения
for message in messages:
    print(message.text)

driver.quit()