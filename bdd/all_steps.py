from pytest_bdd import given, when, then
from fixture.application import *


@given("Open home-page and open registration form")
def registr(app):
    app.start_registration()

@when('I input all required fields "<username>", "<phone>","<email>","<password>"')
def new_user(app, username, phone, email, password):
    app.Open_home_page_1()
    app.open_registration_form()
    app.Registration(username, phone, email, password)

@then("I press submit button and see homepage authorized user")
def verify_register(app):
    app.end_registration()

@given('Open home-page')
def open_home_page(app):
    app.Open_home_page()


@when('Open a login form and login "<username>", "<password>" I logout')
def login_and_logout(app, username, password):
    app.login_in(username, password)
    app.log_out()


@then("I see home page an unauthorized user")
def verify_logout(app):
    app.Unauthorized_user()



