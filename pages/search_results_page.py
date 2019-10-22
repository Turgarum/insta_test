from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultPage(BasePage):
    BUTTON_FOLLOW = (By.XPATH,"//button[@type='button']")

    def get_follow_button_text(self):
        return self.get_element(self.BUTTON_FOLLOW).text
    