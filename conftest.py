from test.loginTest import *
# from fixture.session import SessionHelper
# from fixture.personal_data import *

@pytest.fixture
def app(request):
    fixture = Login()
    return fixture