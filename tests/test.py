from selenium import webdriver
from pages.login_page import LoginPage
driver = webdriver.Chrome('D:\QAA\chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://instagram.com/accounts/login')

my_login_page = LoginPage(driver)
my_login_page.enter_username("turgarom")
my_login_page.enter_password("123456qwe")
my_login_page.click_login()

my_main_page = MainPage(driver)
main_page.type_in_search_field("#fitness")
main_page.click_result_with_text("#fitness")

my_search_page = SearchPage (driver)
assert "Follow" in search_page.get_follow_button_text

