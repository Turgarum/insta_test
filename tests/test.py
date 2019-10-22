from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultPage
import time

driver = webdriver.Chrome('D:\QAA\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://instagram.com/accounts/login')

my_login_page = LoginPage(driver)
my_login_page.enter_username("turgarom")
my_login_page.enter_password("123456qwe")
my_login_page.click_login()

my_main_page = MainPage(driver)
my_main_page.click_not_now_button()
my_main_page.type_in_search_field("#foodporn")
my_main_page.click_result_with_text("#foodporn")



my_search_page = SearchResultPage (driver)

#assert "Подписаться" in my_search_page.get_follow_button_text()
#print (my_search_page.get_follow_button_text())

try:
    if my_search_page.get_follow_button_text():
        print ("Button 'Подписаться' is ready to be clicked")
except:
    print ("Не прокатилло")

driver.close()