from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_info_page(Base):
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name_locator = "//input[@id='first-name']"
    last_name_locator = "//input[@id='last-name']"
    postal_code_locator = "//input[@id='postal-code']"
    continue_locator = "//input[@id='continue']"
    check_word_locator = "//span[contains(text(), 'Checkout: Overview')]"

    # Getters
    def get_fname_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name_locator)))

    def get_lname_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name_locator)))

    def get_postal_code_locator(self):
        return WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH, self.postal_code_locator))))

    def get_continue_locator(self):
        return WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH,
                                                                                 self.continue_locator))))

    def get_check_word(self):
        return WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH, self.check_word_locator))))

    # Actions
    def input_fname(self, firstname):
        self.get_fname_locator().send_keys(firstname)

    def input_lname(self, lastname):
        self.get_lname_locator().send_keys(lastname)

    def input_postal_code(self, postal_code):
        self.get_postal_code_locator().send_keys(postal_code)
        print("Client info inputed")

    def click_continue(self):
        self.get_continue_locator().click()
        print("Continue click")

    # Methods
    def input_client_info_and_continue(self):
        self.get_current_url()
        self.input_fname("Alex")
        self.input_lname("Price")
        self.input_postal_code("390013")
        self.click_continue()
        self.assert_word(self.get_check_word(), "CHECKOUT: OVERVIEW")