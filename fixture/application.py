import time
from selenium.webdriver.chrome.webdriver import WebDriver


class Application:
    def __init__(self):
        # функция предподготовки, стартует преред тестом
        self.wd = WebDriver()
        # self.wd - объект в которой поместили ссылку www.delivery-club.ru
        self.wd.implicitly_wait(60)

    def Open_home_page(self):
        wd = self.wd
        wd.get("http://www.delivery-club.ru/")
        wd.find_element_by_link_text("Вход / Регистрация").click()

    def login_in(self, username, password):
        wd = self.wd
        self.Open_home_page()
        wd.find_element_by_name("c_l").click()
        wd.find_element_by_name("c_l").clear()
        wd.find_element_by_name("c_l").send_keys(username)
        wd.find_element_by_name("c_p").click()
        wd.find_element_by_name("c_p").clear()
        wd.find_element_by_name("c_p").send_keys(password)
        wd.find_element_by_link_text("ВОЙТИ").click()

    def log_out(self):
        wd = self.wd
        wd.find_element_by_css_selector("span.user-profile__span").click()
        wd.find_element_by_link_text("Выход").click()

    def Open_home_page_1(self):
        wd = self.wd
        wd.get("http://www.delivery-club.ru/")


    def Registration(self, new_name, phone, email, password):
        wd = self.wd
        wd.find_element_by_link_text("ЗАРЕГИСТРИРОВАТЬСЯ").click()
        time.sleep(3)
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(new_name)
        wd.find_element_by_name("phone1").click()
        wd.find_element_by_name("phone1").clear()
        wd.find_element_by_name("phone1").send_keys(phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_link_text("ЗАРЕГИСТРИРОВАТЬСЯ").click()
        time.sleep(5)






    def destroy(self):
        self.wd.quit()


        # Содержит все впомогательные методы
