import os
import time

from dotenv import load_dotenv
from selenium import webdriver


load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASS')
URL = os.getenv('URL')
driver = webdriver.Chrome()


def time_sleep_1():
    return time.sleep(1)