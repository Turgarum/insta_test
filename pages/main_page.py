from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    BUTTON_NOT_NOW = (By.XPATH, "//button[text() = 'Не сейчас']")
    FIELD_SEARCH = (By.XPATH, "//input[@placeholder = 'Поиск']")

    def type_in_search_field(self, text):
        self.type_in(self.FIELD_SEARCH, text)

    def click_not_now_button (self):
        self.click_on(self.BUTTON_NOT_NOW)

    def click_result_with_text(self, text):
        RESULT = (By.XPATH,"//span[text()='{}']".format(text))
        #b = "{} and {}".format(text, self.BUTTON_NOT_NOW)
        self.click_on(RESULT)


