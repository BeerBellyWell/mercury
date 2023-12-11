import time

from selenium.webdriver.common.by import By

from options import driver, LOGIN, PASSWORD, URL, time_sleep_1


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

        # Выбрать предприятие - Магазин "Греция"
        driver.find_element(By.XPATH,
            '//*[@id="body"]/form/table/tbody/tr[1]/td/div/label[2]'
        ).click()

        # Нажать кнопку
        driver.find_element(By.XPATH,
            '//*[@id="body"]/form/table/tbody/tr[2]/td/div/button[1]'
        ).click()

        return True
    
    except:
        return False
