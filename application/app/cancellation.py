import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from core.settings import driver, time_sleep_1_sec, logger


def cancellation() -> bool:
    """Cancels invoices from the production journal"""
    # Navigate to the production journal
    driver.find_element(By.XPATH, '//*[@id="main-menu"]/ul/li[4]/a').click()
    time_sleep_1_sec()

    # Click on 'Sent'
    driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td[1]/ul/li/ul/li[2]/a').click()
    time_sleep_1_sec()

    # Check if the list is empty
    try:
        elem = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/h4')
        if elem:
            logger.info('Cancellation of invoices successfully completed.')
            return False

    except NoSuchElementException:
        # Select the first invoice
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/table/tbody/tr[2]/td[13]/a').click()
        time_sleep_1_sec()

        # Cancel the invoice
        driver.find_element(By.XPATH, '//tbody/tr/td/div/button[1]').click()
        time_sleep_1_sec()

        # Confirm cancellation in the pop-up window
        Alert(driver).accept()
        time_sleep_1_sec()

        # Enter "Goods sold"
        driver.find_element(By.ID, 'whyRevoked').send_keys('Товар продан.')
        time_sleep_1_sec()

        # Close the pop-up for cancellation
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/table/tbody/tr[6]/td/form/div[2]/div/div/div[2]/button[1]').click()
        time.sleep(3)

        return True
