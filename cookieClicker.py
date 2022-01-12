from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

five_minutes_ahead = time.time() + 300

s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
menu_items = driver.find_elements(By.CSS_SELECTOR, "div#store b")

item_list = [item.text for item in menu_items[:-1]]
item_prices = []
cps = None

for item_a in item_list:
    item_split = item_a.split(" ")
    item_prices.append(int(locale.atoi(item_split[-1])))

while time.time() < five_minutes_ahead:
    x = 0
    five_seconds = time.time() + 5
    total_cookies = int(locale.atoi(driver.find_element(By.ID, "money").text))

    while time.time() < five_seconds:
        cookie.click()

    total_cookies = int(locale.atoi(driver.find_element(By.ID, "money").text))
    for number in item_prices:

        if total_cookies > number:
            highest_index = item_prices.index(number)

    menu_items = driver.find_elements(By.CSS_SELECTOR, "div#store b")
    print(f"Purchased: {menu_items[highest_index].text}")
    menu_items[highest_index].click()
    cps = driver.find_element(By.ID, "cps").text
    
print(cps)







