import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.payment_page import Payment_page


@pytest.mark.run(order=1)
def test_buy_product_1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='/Users/zordex/PyProjects/python_selenium/chromedriver',
                              options=options)
    print("Start test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_info_page(driver)
    cip.input_client_info_and_continue()

    pp = Payment_page(driver)
    pp.payment()

    fp = Finish_page(driver)
    fp.finish()
    print("Finish test 1")


@pytest.mark.run(order=2)
def test_buy_product_2():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='/Users/zordex/PyProjects/python_selenium/chromedriver',
                              options=options)
    print("Start test 2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_info_page(driver)
    cip.input_client_info_and_continue()

    pp = Payment_page(driver)
    pp.payment()

    fp = Finish_page(driver)
    fp.finish()

    print("Finish test 2")


@pytest.mark.run(order=3)
def test_buy_product_3():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='/Users/zordex/PyProjects/python_selenium/chromedriver',
                              options=options)
    print("Start test 3")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_info_page(driver)
    cip.input_client_info_and_continue()

    pp = Payment_page(driver)
    pp.payment()

    fp = Finish_page(driver)
    fp.finish()
    print("Finish test 3")