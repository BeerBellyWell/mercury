# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert
# from selenium.common import exceptions

from auth import auth
from cancellation import cancellation
from saving import saving
from change_company import change_company

from options import driver, time_sleep_1


def main():
    """Основная работа программы"""
    if auth() == False:
        return 'auth - Работа окончена с ошибкой!'

    time_sleep_1()

    while cancellation():
        pass

    print('Аннулирование накладных в греции прошло успешно!')

    while saving():
        pass
    
    print('Сохранение накладных в греции прошло успешно!')
    time_sleep_1()

    # ПЕРЕХОД В ДРУГОЕ ПРЕДПРИЯТИЕ!

    if change_company() == False:
        return 'change company - Работа окончена с ошибкой!'
    
    while cancellation():
        pass

    print('Аннулирование накладных в "Елизово ОПТ" прошло успешно!')

    while saving():
        pass
    
    print('Сохранение накладных в "Елизово ОПТ" прошло успешно!')

    driver.close()
    driver.quit()
 
    return 'main - Работа окончена!'


if __name__ == '__main__':
    print(main())
