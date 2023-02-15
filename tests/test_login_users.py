import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from pages.login_page import Login_page
from pages.main_page import Main_page

# Test users logins:
users = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]


def test_all_users():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='/Users/zordex/PyProjects/python_selenium/chromedriver',
                              options=options)
    print("Start all users test")
    lp = Login_page(driver)
    mp = Main_page(driver)
    login_count = 0  # создаю счетчик пройденных тестов для удобочитаемости логов и отладки
    for user in users:
        try:
            lp.authorization_custom(user)
        except TimeoutException:
            if user == "locked_out_user":
                # решаю сделать проверку на locked user'а по значению из list users, был вариант ещё
                # сделать через element.text() когда выкидывает error button, но когда login locked user'а
                # четко определён, то смысла в этом нет.
                print("Locked user detected")
                login_count += 1
                print(f"Test {login_count} successfuly done")
                continue
            else:
                break
        finally:
            pass
        mp.logout()
        login_count += 1
        print(f"Test №{login_count} successfuly done")





