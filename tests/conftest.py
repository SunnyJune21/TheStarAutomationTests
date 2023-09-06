import pytest as pytest
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def get_new_user_credentials():
    current_time_seconds = int(time.time())
    email = f"test{current_time_seconds}@test.com"
    postal_code = "M5V0H8"
    first_name = "Justine"
    last_name = "Test"
    password = "eonbfdsml3980TIO!$"
    return [email, postal_code, first_name, last_name, password]

@pytest.fixture(scope="function")
def get_existing_credentials():
    email = "test12357@test.com"
    password = "eonbfdsml3980TIO!$"
    name = "Jenny"
    postal_code = "M5V0H8"
    phone = "6578901234"
    country = "Canada"
    return [email, password, name, postal_code, phone, country]

@pytest.fixture(scope="function")
def sign_in_with_wrong_password():
    email = "test12357@test.com"
    password = "password"
    return [email, password]

@pytest.fixture(scope="function")
def sign_in_with_wrong_email():
    email = "test12357@testtest.com"
    password = "eonbfdsml3980TIO!$"
    return [email, password]

@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()
