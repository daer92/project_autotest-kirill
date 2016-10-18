#
#
# class SessionHelper:
#     def __init__(self, app):
#         self.app = app
#
#
#
# def login_in(self, username, password):
#     wd = self.app.wd
#     self.app.Open_home_page()
#     wd.find_element_by_name("c_l").click()
#     wd.find_element_by_name("c_l").clear()
#     wd.find_element_by_name("c_l").send_keys(username)
#     wd.find_element_by_name("c_p").click()
#     wd.find_element_by_name("c_p").clear()
#     wd.find_element_by_name("c_p").send_keys(password)
#     wd.find_element_by_link_text("ВОЙТИ").click()
#
# def log_out(self):
#     wd = self.app.wd
#     wd.find_element_by_css_selector("span.user-profile__span").click()
#     wd.find_element_by_link_text("Выход").click()
#
# def