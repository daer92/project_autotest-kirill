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

    def destroy(self):
        self.wd.quit()


        # Содержит все впомогательные методы
