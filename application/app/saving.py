import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from core.settings import driver, time_sleep_1_sec, logger


def saving() -> bool:
    """Repayment and save new invoices"""
    # Navigate to veterinary documents
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[3]/ul/li[7]/a').click()
    time_sleep_1_sec()

    # Click on Incoming - processed
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/table/tbody/tr/td[3]/ul/li/ul/li[1]/a').click()
    time_sleep_1_sec()

    # Check if the list is empty
    try:
        elem = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div[2]/h4')
        if elem:
            logger.info('Repayment and saving of invoices is completed.')
            return False

    except NoSuchElementException:
        # Select all
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div[1]/ul/li[2]/input').click()
        time_sleep_1_sec()

        # Batch settlement
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div[1]/ul/li[8]/span').click()
        time_sleep_1_sec()

        # Confirm conditions
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/table/tr[1]/td/table/tr[3]/td[2]/label').click()
        time_sleep_1_sec()

        # Click execute
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/table/tr[2]/td/div/button[2]').click()
        time.sleep(10)

        # Close
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/table/tr[3]/td/div/button').click()
        time_sleep_1_sec()

        return True
