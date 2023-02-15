from selenium.common import NoSuchWindowException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.main_page import Main_page


class Login_page(Base):
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    username_locator = "//input[@id='user-name']"
    password_locator = "//input[@id='password']"
    login_button_locator = "//input[@id='login-button']"
    check_word_locator = "//span[@class='title']"
    error_button = "//button[@class='error-button']"

    # Getters

    def get_username(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.username_locator)))

    def get_password(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.login_button_locator)))

    def get_check_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.check_word_locator)))

    # Actions

    def input_username(self, username):
        self.get_username().send_keys(username)
        print("Input username")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_username("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_check_word(), "PRODUCTS")

    def authorization_custom(self, username):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_username(username)
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_check_word(), "PRODUCTS")