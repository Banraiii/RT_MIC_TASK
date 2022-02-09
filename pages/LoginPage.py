from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .BasePage import BasePage
from .locators import LoginPageLocators
import allure
from allure_commons.types import AttachmentType


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    @allure.step('Авторизация')
    def should_be_authorization_form(self):
        draft = self.should_be_login_field()
        draft2 = self.should_be_password_field()
        if not draft or not draft2:
            with allure.step('Скриншот ошибки'):
                allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot'
                              , attachment_type=AttachmentType.PNG)
        assert draft
        assert draft2

    def should_be_login_field(self):
        assert self.is_element_present_and_can_be_click(*LoginPageLocators.LOGIN_FIELD), 'Нет строки логина.'
        return True

    def should_be_password_field(self):
        assert self.is_element_present_and_can_be_click(*LoginPageLocators.PASSWORD_FIELD), 'Нет строки пароля.'
        return True

    @allure.step('Ввод данных')
    def insert_value_into_form(self, log, passw):
        draft = self.put_text_in_field(*LoginPageLocators.LOGIN_FIELD, log)
        draft2 = self.put_text_in_field(*LoginPageLocators.PASSWORD_FIELD, passw)
        if not draft or not draft2:
            with allure.step('Скриншот ошибки'):
                allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot'
                              , attachment_type=AttachmentType.PNG)
        assert draft, 'Ошибка, на этапе вставки login'
        assert draft2, 'Ошибка, на этапе вставки password'

    @allure.step('Поиск кнопки')
    def should_be_enter_btn(self):
        draft = self.is_element_present_and_can_be_click(
            *LoginPageLocators.SEND_AUTHORIZATION_FORM_BTN)
        if not draft:
            with allure.step('Скриншот ошибки'):
                allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot'
                              , attachment_type=AttachmentType.PNG)
        assert self.is_element_present_and_can_be_click(
            *LoginPageLocators.SEND_AUTHORIZATION_FORM_BTN), 'Нет конпки ВОЙТИ в форме авторизации.'

    @allure.step('Нажатие кнопки «Войти»')
    def send_form_vie_enter_btn(self):
        draft = self.click_on_element(
            *LoginPageLocators.SEND_AUTHORIZATION_FORM_BTN)
        if not draft:
            with allure.step('Скриншот ошибки'):
                allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot'
                              , attachment_type=AttachmentType.PNG)
        assert draft, 'Кнопка "Войти" не может быть нажата.'

    @allure.step('Отсутствие сообщения об ошбке')
    def should_not_be_error_message(self):
        draft = self.is_element_present_and_can_be_click(
            *LoginPageLocators.ERROR_MESSAGE)
        if draft:
            with allure.step('Скриншот ошибки'):
                allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot'
                              , attachment_type=AttachmentType.PNG)
        assert not draft, \
            'Полученно сообщение об ошибке: "Ошибка авторизации!"'
