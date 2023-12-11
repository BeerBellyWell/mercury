import time

from selenium.webdriver.common.by import By

from options import driver, time_sleep_1


def saving():
    """Погасить и сохранить новые накладные"""

    # Ветеринарные документы
    driver.find_element(By.XPATH,
        '/html/body/div[1]/div/div[1]/div[2]/div[3]/ul/li[7]/a').click()
    time_sleep_1()

    # Входящие - оформленные
    driver.find_element(By.XPATH,
        '/html/body/div[1]/div/div[3]/table/tbody/tr/td[3]/ul/li/ul/li[1]/a').click()
    time_sleep_1()

    # Если есть элемент "Список пуст"
    try:
        elem = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div[2]/h4')
        if elem:
            return False
    except:
        # Выделить все
        driver.find_element(By.XPATH,
            '/html/body/div[1]/div/div[3]/form/div[1]/ul/li[2]/input').click()
        time_sleep_1()

        # Пакетное гашение
        driver.find_element(By.XPATH,
            '/html/body/div[1]/div/div[3]/form/div[1]/ul/li[8]/span').click()
        time_sleep_1()

        # Подтверждаю выполнение перечисленных условий
        driver.find_element(By.XPATH,
            '/html/body/div[1]/div/div[3]/div/table/tr[1]/td/table/tr[3]/td[2]/label').click()
        time_sleep_1()

        # Нажать выполнить
        driver.find_element(By.XPATH,
            '/html/body/div[1]/div/div[3]/div/table/tr[2]/td/div/button[2]').click()
        time.sleep(10)

        # Закрыть
        driver.find_element(By.XPATH,
            '/html/body/div[1]/div/div[3]/div/table/tr[3]/td/div/button').click()
        time_sleep_1()

        return True
