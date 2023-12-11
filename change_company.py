from selenium.webdriver.common.by import By

from options import driver, time_sleep_1


def change_company():
    try:
        # Сменить предприятие
        driver.find_element(By.XPATH,
            '/html/body/div[1]/div/div[1]/div[1]/div[2]/ul/li[4]/a').click()
        time_sleep_1()

        # Выбрать предприятие - Магазин "Елизово ОПТ"
        driver.find_element(By.XPATH,
            '/html/body/div[1]/div/div[3]/form/table/tbody/tr[1]/td/div/label[3]').click()
        time_sleep_1()

        # Нажать кнопку Выбрать
        driver.find_element(By.XPATH,
            '//*[@id="body"]/form/table/tbody/tr[2]/td/div/button[1]').click()
        time_sleep_1()

        return True
    
    except:
        return False
