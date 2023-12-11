import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from options import driver, time_sleep_1


def cancellation():
    """Аннулирование накладных из журнала продукции"""

    # Журнал продукции
    driver.find_element(By.XPATH, '//*[@id="main-menu"]/ul/li[4]/a').click()
    time_sleep_1()

    # Отправленные
    driver.find_element(By.XPATH,
        '//*[@id="body"]/table/tbody/tr/td[1]/ul/li/ul/li[2]/a'
    ).click()
    time_sleep_1()

    # Если есть элемент "Список пуст"
    try:
        elem = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/h4')
        if elem:
            return False

    except:
        # Выбрать первую накладную
        driver.find_element(By.XPATH,
            '/html/body/div[1]/div/div[3]/form/div/table/tbody/tr[2]/td[13]/a'
        ).click()
        time_sleep_1()

        # Аннулировать
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
