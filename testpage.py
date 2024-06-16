import logging
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_POST_BTN = (By.CSS_SELECTOR, """#create-btn""")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST_BTN = (By.CSS_SELECTOR, """#create-item > div > div > div:nth-child(7) > div > button > span""")
    LOCATOR_NEW_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, """#app > main > nav > ul > li:nth-child(2) > a""")
    LOCATOR_CONTACT_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_MAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_SEND_BTN = (By.CSS_SELECTOR, """#contact > div.submit > button > span""")

class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

# ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_LOGIN_FIELD, word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_PASS_FIELD, word, description="password form")

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_TITLE, word, description="title form")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_DESCRIPTION, word, description="description form")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTENT, word, description="content form")

    def enter_contact_name(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTACT_NAME, word, description="contact name form")

    def enter_contact_mail(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTACT_MAIL, word, description="contact mail form")

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTACT_CONTENT, word, description="contact content form")

# CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.LOCATOR_LOGIN_BTN,description="login")

    def click_new_post_btn(self):
        self.click_button(TestSearchLocators.LOCATOR_NEW_POST_BTN, description="new post")

    def click_save_post_btn(self):
        self.click_button(TestSearchLocators.LOCATOR_SAVE_POST_BTN, description="save")

    def click_contact_link(self):
        self.click_button(TestSearchLocators.LOCATOR_CONTACT_BTN, description="contact")

    def click_contact_send_btn(self):
        self.click_button(TestSearchLocators.LOCATOR_CONTACT_SEND_BTN, description="send")

# GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_ERROR_FIELD, description="401")

    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_HELLO, description="user page")

    def get_title_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_NEW_TITLE, description="user title")

    def get_alert(self):
        logging.info("Set alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text
