import os
import time

from loguru import logger
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASS')
URL = os.getenv('URL')

logger.add("../logs/log_{time}_file.log", mode="w")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def time_sleep_1_sec():
    return time.sleep(1.5)
