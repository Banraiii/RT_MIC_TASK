from pages.SpeedPage import SpeedPage
from utils import ConfigReader
import time
import pytest


@pytest.mark.all_test
@pytest.mark.parametrize('four_limit',
            list(ConfigReader.get_config()['speed info']['time_limit_four'].split(',')) )
@pytest.mark.parametrize('speed_limeted_seven',
            list(ConfigReader.get_config()['speed info']['speed_limited'].split(',')) )
def test_measuring_internet_speed(speed_driver, four_limit, speed_limeted_seven):
    speed_page = SpeedPage(speed_driver, ConfigReader.get_config()['speed info']['first_url'])
    speed_page.open()
    speed_page.should_be_btn()
    speed_page.go_to_action()
    speed_page.should_be_action_finished(four_limit)
    result_speed = speed_page.get_result_speed_test()
    speed_page.result_should_be_equal_digit(speed_limeted_seven, result_speed)