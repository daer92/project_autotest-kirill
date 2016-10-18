# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application() # Инициализация, создание фикстуры.
    request.addfinalizer(fixture.destroy) # Указание на разрушение фикстуры
    return fixture


def test_(app): # тестовый метод вызывающий фикстуру
    # параметры и вспомогательные методы
    app.login_in(username="daer92@gmail.com", password="kirill92")
    app.log_out()

def test_invalid_login(app): # тестовый метод вызывающий фикстуру
    # параметры и вспомогательные методы
    app.login_in(username="w@w.com", password="111111")
    app.log_out()

def test_new_name(app):
    app.Open_home_page_1()
    app.Registration(new_name="Test", phone="4444444444", email="qwer1@gmail.com", password="qwert12345rewqq")
