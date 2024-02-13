from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from core.settings import driver, time_sleep_1_sec, logger


def change_company() -> bool:
    '''Change the company from Greece to Elizovo OPT'''
    try:
        logger.info('Initiating company change.')
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/ul/li[4]/a').click()
        time_sleep_1_sec()

        # Select "Elizovo OPT" company
        driver.find_element(By.XPATH, '//*[@id="body"]/form/div/div[1]/div/label[3]').click()
        time_sleep_1_sec()

        # Click the "Select" button
        driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()
        time_sleep_1_sec()

        return True

    except NoSuchElementException as e:
        logger.error(f'Failed to switch to another company: {str(e)}')
        return False
