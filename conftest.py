import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import ConfigReader
import sys


# sections = {
#     'speed_test': 'speed info',
#     'test_site': 'manydomain info'
# }
#
# user_params = {
#     'first_url': 'first_url',
#     'id': '1'
# }
#
#
#
# special_url = ConfigReader.get_setting(ConfigReader.config_path, sections['speed_test'], user_params['first_url'])
# base_url = ConfigReader.get_setting(ConfigReader.config_path, sections['test_site'], user_params['id'])

def pytest_addoption(parser):
    parser.addoption('--fl', action='store',
                     default="chrome", help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default="en",
                     help='Выберите язык ="es" ')
    parser.addoption('--browser_name', action='store',
                     default="chrome", help='Choose browser: chrome or firefox')
    # parser.addoption('--url', '-U', action='store', default=base_url)


def teak_list():
    list2 = list(ConfigReader.get_config()['manydomain info'])
    res = []
    for i in (sys.argv[-1][sys.argv[-1].find('--fl=')+5:len(sys.argv[-1])]).split(','):
        if i in list2:
            res.append(i)
    if res == []:
        res = list2
    return res

@pytest.fixture(scope="function")
def speed_driver(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(options=options)
        # driver.get(special_url)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
        driver.get(request.config.getoption('--url'))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser")
    driver.quit()


@pytest.fixture(scope="function")
def driver(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(options=options)
        # driver.get(base_url)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
        driver.get(request.config.getoption('--url'))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser")
    driver.quit()
