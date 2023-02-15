from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    add_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    add_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    add_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    menu_button = "//button[@id='react-burger-menu-btn']"
    about_link = "//a[@id='about_sidebar_link']"
    logout_link = "//a[@id='logout_sidebar_link']"

    # Locators getters
    def get_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_product_2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_about_link(self):
        return WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH, self.about_link))))

    def get_logout_link(self):
        return WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH, self.logout_link))))

    # Actions
    def click_product_1(self):
        self.get_product_1().click()
        print("Add product 1 to cart")

    def click_product_2(self):
        self.get_product_2().click()
        print("Add product 2 to cart")

    def click_product_3(self):
        self.get_product_3().click()
        print("Add product 3 to cart")

    def go_cart(self):
        self.get_cart().click()
        print("Go to cart")

    def click_menu(self):
        self.get_menu_button().click()

    def click_about_link(self):
        self.get_about_link().click()

    def click_logout_link(self):
        self.get_logout_link().click()

    # Methods

    def select_product_1(self):
        self.get_current_url()
        self.click_product_1()
        self.go_cart()

    def select_product_2(self):
        self.get_current_url()
        self.click_product_2()
        self.go_cart()

    def select_product_3(self):
        self.get_current_url()
        self.click_product_3()
        self.go_cart()

    def logout(self):
        self.click_menu()
        self.click_logout_link()


