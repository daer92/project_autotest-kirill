# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
import time, unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_(self):
        wd = self.wd
        self.Open_home_page(wd)
        self.login_in(wd, username="daer92@gmail.com", password="kirill92")
        self.log_out(wd)

    def test_invalid_login(self):
        wd = self.wd
        self.Open_home_page(wd)
        self.login_in(wd, username="w@w.com", password="111111")
        self.log_out(wd)

    def log_out(self, wd):
        wd.find_element_by_css_selector("span.user-profile__span").click()
        wd.find_element_by_link_text("Выход").click()


    def login_in(self, wd, username, password):
        wd.find_element_by_name("c_l").click()
        wd.find_element_by_name("c_l").clear()
        wd.find_element_by_name("c_l").send_keys(username)
        wd.find_element_by_name("c_p").click()
        wd.find_element_by_name("c_p").clear()
        wd.find_element_by_name("c_p").send_keys(password)
        wd.find_element_by_link_text("ВОЙТИ").click()

    def Open_home_page(self, wd):
        wd.get("http://www.delivery-club.ru/")
        wd.find_element_by_link_text("Вход / Регистрация").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
