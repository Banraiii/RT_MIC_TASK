from selenium.webdriver.common.by import By


class SpeedPageLocators():
	MEASURE_BTN = (By.XPATH, '//div[@class="measurement layout__measurement"]//button')
	AGAIN_MEASURE_BTN = (By.XPATH, '//div[@class="load-box__row load-box__row_type_main load-box__row_clear"]//span[text()="Измерить ещё раз"]')
	INCOMING_CONNECTION = (By.XPATH, '//div[@class="speed-progress-bar__left"]//div[1]')

class LoginPageLocators():
	LOGIN_FIELD = (By.XPATH, '//form/div/input')
	PASSWORD_FIELD = (By.XPATH, '//form//input[@id="promed-password"]')
	SEND_AUTHORIZATION_FORM_BTN  = (By.XPATH, '//form//button[@id="auth_submit"]')
	ERROR_MESSAGE = (By.CSS_SELECTOR, '#login-message')