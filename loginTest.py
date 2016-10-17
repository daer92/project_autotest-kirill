# -*- coding: utf-8 -*-
import unittest
from application import Application
import pytest

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
