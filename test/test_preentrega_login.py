import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login

@pytest.mark.login
def test_login(chrome_driver):
    login(chrome_driver)