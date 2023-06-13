from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from unittest import TestCase, main




driver = webdriver.Chrome(executable_path='')

class TestAutYandex(TestCase):
    
    def setUp(self):
        self.url = 'https://passport.yandex.ru/auth/'
        self.login = ''
        self.password = ''

    def test_login(self):
        driver.get(self.url)
        time.sleep(2)
        email_input = driver.find_element(By.ID, 'passp-field-login')
        email_input.clear()
        email_input.send_keys(self.login)
        time.sleep(2)
        clic_but = driver.find_element(By.ID, 'passp:sign-in').click()
        time.sleep(1)
        self.assertTrue('Войдите, чтобы продолжить' in driver.page_source)
        time.sleep(5)

    def test_password(self):
        pass_input = driver.find_element(By.ID, 'passp-field-passwd')
        pass_input.clear()
        pass_input.send_keys(self.password)
        time.sleep(2)
        clic_but = driver.find_element(By.ID, 'passp:sign-in').click()
        time.sleep(5)
        self.assertTrue('Данные' in driver.page_source)
        time.sleep(5)
        driver.close()
        driver.quit()
