from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application() # Инициализация, создание фикстуры.
    request.addfinalizer(fixture.destroy) # Указание на разрушение фикстуры
    return fixture