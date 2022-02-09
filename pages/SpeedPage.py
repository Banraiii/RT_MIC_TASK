from .BasePage import BasePage
from .locators import SpeedPageLocators
import allure
from allure_commons.types import AttachmentType


class SpeedPage(BasePage):
	def __init__(self, *args, **kwargs):
		super(SpeedPage, self).__init__(*args, **kwargs)

	@allure.step('Найти кнопку «Измерить»')
	def should_be_btn(self):
		draft = self.is_element_present_and_can_be_click(*SpeedPageLocators.MEASURE_BTN)
		if not draft:
			with allure.step('Скриншот ошибки'):
				allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot'
							  , attachment_type=AttachmentType.PNG)
		assert draft, "Нет кнопки 'Измерить' на этапе поиска"

	@allure.step('Нажать кнопку «Измерить»')
	def go_to_action(self):
		assert self.click_on_element(*SpeedPageLocators.MEASURE_BTN), "Упал на этапе нажатия кнопки"

	@allure.step('Дождаться выполнения замеров.')
	def should_be_action_finished(self, four_limit):
		assert self.is_element_present_and_can_be_click(*SpeedPageLocators.AGAIN_MEASURE_BTN, four_limit), "Нет кнопки «Измерить ещё раз» на этапе поиска"

	@allure.step('Результат «Входящее соединение»')
	def get_result_speed_test(self):
		result = self.get_element_text(*SpeedPageLocators.INCOMING_CONNECTION)
		assert result, "Нет текста, результата входящего соединения"
		return result.split(' ')[0]

	@allure.step('Значение скорости не менее «N»')
	def result_should_be_equal_digit(self, digit, received_digit):
		assert float(received_digit) >= float(digit), f"Скокрость соединения менее {digit}" 