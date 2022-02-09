from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoAlertPresentException, NoSuchElementException
import utils.basicLogger as bl
import time

import allure
from allure_commons.types import AttachmentType
from utils import ConfigReader

stand_time = ConfigReader.get_config()['general info']['standard_waiting_time']


class BasePage():
    log = bl.loggen()
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    @allure.story('Проверка пристувия элемента, на странице с ожиданием')
    @allure.severity('critical')
    def is_element_present_and_can_be_click(self, how, what, timeout=stand_time):
        try:
            ec = EC.element_to_be_clickable((how, what))
            WebDriverWait(self.driver, timeout).until(ec)
            self.log.info(f'selector: found')
        except TimeoutException:
            self.log.info(f'selector: {(how, what)} not found')
            return False
        return True

    def is_not_element_present(self, how, what, timeout=stand_time):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=stand_time):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def text_should_be_in_currnet_url(self, text):
        if text in self.driver.current_url:
            return True
        return False

    def put_text_in_field(self, how, what, text):
        try:
            field = self.driver.find_element(how, what)
            field.send_keys(f'{text}')
        except NoSuchElementException:
            return False
        return True

    def click_on_element(self, how, what):
        try:
            element = self.driver.find_element(how, what)
            element.click()
        except:
            return False
        return True

    def first_el_list_elements_equal_two_element_by_text(self, how, what, how_two, what_two, num):
        try:
            if str(self.driver.find_elements(how, what)[num].text) == str(
                    self.driver.find_element(how_two, what_two).text):
                return True
            return False
        except NoSuchElementException:
            return False

    def elements_n_text_equal_text(self, num, how, what, text1):
        try:
            if str(self.driver.find_elements(how, what)[num].text) == text1:
                return True
            return False
        except NoSuchElementException:
            return False

    def get_element_text(self, how, what):
        try:
            if str(self.driver.find_element(how, what).text):
                return self.driver.find_element(how, what).text
            return False
        except NoSuchElementException:
            self.log.info(f'selector: {(how, what)} not found')
            return False
