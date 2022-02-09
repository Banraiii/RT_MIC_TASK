from pages.LoginPage import LoginPage
import pytest
import sys
from utils import ConfigReader
import allure
from conftest import teak_list

@pytest.mark.all_test
@pytest.mark.parametrize('id',teak_list())
def test_user_can_log_in(driver, id):
	config_data = ConfigReader.get_config()['manydomain info'][id].split(',')
	login_page = LoginPage(driver, str(config_data[0]))
	login_page.open()
	login_page.should_be_authorization_form()
	login_page.insert_value_into_form(config_data[1], config_data[2])
	login_page.should_be_enter_btn()
	login_page.send_form_vie_enter_btn()
	login_page.should_not_be_error_message()
