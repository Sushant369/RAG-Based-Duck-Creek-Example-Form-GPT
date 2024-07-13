from app import *  # Ensure to import your Flask app correctly
from selenium.webdriver.common.by import By

def test_index_page(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200  # Assert the response status code
    assert b'<!DOCTYPE html>' in response.data  # Check if the response contains HTML content


def test_chatbot(driver):
    """Tests the fields and response of the chatbot"""

    driver.get("https://dct-forms-mate-faaff5c2e205.herokuapp.com/")

    driver.find_element(By.ID, "user-input").send_keys("Hi Tell me about the Duck Creek Forms")

    driver.find_element(By.ID, "enterBtn").click()
    
    after_click_user_text = driver.find_element(By.CLASS_NAME, "user-message").text
    after_click_bot_text = driver.find_element(By.CLASS_NAME, "bot-message").text

    assert (after_click_user_text == "Hi Tell me about the Duck Creek Forms") and (after_click_bot_text is not None)
