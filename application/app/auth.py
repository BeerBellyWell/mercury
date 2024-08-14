from selenium.webdriver.common.by import By
from core.settings import driver, LOGIN, PASSWORD, URL, time_sleep_1_sec, logger


def auth() -> bool:
    """Authentication"""
    try:
        logger.info('Authentication.')
        driver.get(url=URL)
        driver.find_element(By.LINK_TEXT, 'Меркурий.ХС').click()
        driver.find_element(By.ID, 'username').send_keys(LOGIN)
        driver.find_element(By.ID, 'password').send_keys(PASSWORD)
        time_sleep_1_sec()
        driver.find_element(By.CLASS_NAME, 'btn.login-btn.btn-success').click()

        # Sleep for manual CAPTCHA entry
        # time.sleep(30)

        # Select the "Greece" store
        driver.find_element(By.XPATH, '//*[@id="body"]/form/div/div[1]/div/label[2]').click()
        time_sleep_1_sec()

        # Click on the Select button
        driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()
        logger.info('Authentication successful.')
        time_sleep_1_sec()

        return True

    except Exception as e:
        logger.info(f'Error during authentication: {str(e)}')
        return False
