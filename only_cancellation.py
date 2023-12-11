'''
Файл только для аннулирования накладных греции
'''

import os
import time

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common import exceptions


# exceptions.NoSuchElementException
load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASS')
URL = os.getenv('URL')
driver = webdriver.Chrome()


def time_sleep_1():
    return time.sleep(1)


def auth():
    """Аутентификация"""
    try:
        # Заходим логинимся
        driver.get(url=URL)
        driver.find_element(By.LINK_TEXT, 'Меркурий.ХС').click()
        driver.find_element(By.ID, 'username').send_keys(LOGIN)
        driver.find_element(By.ID, 'password').send_keys(PASSWORD)
        time_sleep_1()
        driver.find_element(By.CLASS_NAME, 'btn.login-btn.btn-success').click()

        # sleep для того чтобы ввести капчу вручную
        time.sleep(30)

        # Выбрать Грецию
        driver.find_element(By.XPATH,
            '//*[@id="body"]/form/table/tbody/tr[1]/td/div/label[2]'
        ).click()

        # Нажать кнопку
        driver.find_element(By.XPATH,
            '//*[@id="body"]/form/table/tbody/tr[2]/td/div/button[1]'
        ).click()

        return True
    
    except:
        print('В блоке аутентификации что-то пошло не так.')
        return False


def сancellation():
    """Аннулирование накладных"""
    try:
        # Журнал продукции
        driver.find_element(By.XPATH, '//*[@id="main-menu"]/ul/li[4]/a').click()
        time_sleep_1()

        # Отправленные
        driver.find_element(By.XPATH,
            '//*[@id="body"]/table/tbody/tr/td[1]/ul/li/ul/li[2]/a'
        ).click()
        time_sleep_1()

        try:
            # Выбрать первую накладную
            driver.find_element(By.XPATH,
                '/html/body/div[1]/div/div[3]/form/div/table/tbody/tr[2]/td[13]/a'
            ).click()

        except exceptions.NoSuchElementException:
            print('Накладных нет!')
            return False

        # Аннулировать
        time_sleep_1()
        driver.find_element(By.XPATH,
            '//tbody/tr/td/div/button[2]'
        ).click()
        # /html/body/div[1]/div/div[3]/table/tbody/tr[15]/td/div/button[2]
        time_sleep_1()

        # Нажать ОК в сплывающем окне
        Alert(driver).accept()
        time_sleep_1()

        # Ввести "Товар продан"
        driver.find_element(By.ID, 'whyRevoked').send_keys('Товар продан')
        time_sleep_1()

        # Аннулировать всплывашку
        driver.find_element(By.XPATH,
            '/html/body/div[1]/div/div[3]/table/tbody/tr[6]/td/form/div[2]/div/div/div[2]/button[1]'
        ).click()
        time.sleep(3)

        return True
    
    except:
        print('В блоке аннулирования что-то пошло не так.')
        return False


def main():
    """Основная работа программы"""
    if auth() == False:
        return 'Работа окончена!'

    time_sleep_1()

    while сancellation() != False:
        pass

    

    return 'main - Работа окончена!'


if __name__ == '__main__':
    print(main())
