from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class HWSelenium:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def invalid_login_without_input(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == "Epic sadface: Username is required"
        print(f"Invalid Login Without Username and Password | Do Error Messages Match :  {test_result}")

    def invalid_login_without_pw(self):
        sleep(1)
        self.driver.refresh()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == "Epic sadface: Password is required"
        print(f"Invalid Login Without Password | Do Error Messages Match :  {test_result}")

    def invalid_login_by_blocking_user(self):
        sleep(1)
        self.driver.refresh()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("locked_out_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        error_message = (
            self.driver.find_element(By.CSS_SELECTOR,
                                     "#login_button_container > div > form > div.error-message-container.error > h3"))
        test_result = error_message.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Invalid Login By Blocking User | Do Error Messages Match :  {test_result}")

    def valid_login_checking_prod_amount(self):
        sleep(1)
        self.driver.refresh()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        sleep(1)
        prod_card = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        total_prod_card = len(prod_card)
        print("total products on screen: ", total_prod_card)
        print(type(total_prod_card))
        test_result = total_prod_card == 6
        print(f"Valid Login and Counting Prods In Screen | Is it 6 :  {test_result}")

    def adding_removing_prod_to_cart(self):
        sleep(1)
        self.driver.refresh()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        sleep(1)

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_backpack = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_backpack.click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id=\"shopping_cart_container\"]/a")))
        cart_button = self.driver.find_element(By.XPATH, "//*[@id=\"shopping_cart_container\"]/a")
        cart_button.click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        amount_in_cart = len(cart_items)
        assert amount_in_cart
        print("First product added to cart")
        sleep(4)

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, "remove-sauce-labs-backpack")))
        remove_backpack = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_backpack.click()
        sleep(3)
        self.driver.refresh()
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        amount_in_cart = len(cart_items)
        if amount_in_cart == 0:
            print("Cart is empty")
        else:
            print("DEFECT: Product removing failed...")


testClass = HWSelenium()
testClass.invalid_login_without_input()
testClass.invalid_login_without_pw()
testClass.invalid_login_by_blocking_user()
testClass.valid_login_checking_prod_amount()
testClass.adding_removing_prod_to_cart()
