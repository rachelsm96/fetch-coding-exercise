from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


def click_reset():
    driver.find_element(By.XPATH, "//button[text()='Reset']").click()


def click_weigh():
    driver.find_element(By.ID, "weigh").click()


def insert_value_in_left_board(num: str):
    driver.find_element(By.CSS_SELECTOR, "input#left_0").send_keys(num)


def insert_value_in_right_board(num: str):
    driver.find_element(By.CSS_SELECTOR, "input#right_0").send_keys(num)


def get_result() -> str:
    WebDriverWait(driver, 5).until_not(EC.text_to_be_present_in_element_attribute(
        (By.CSS_SELECTOR, "[class=result] button"), "textContent", "?"))
    return driver.find_element(By.CSS_SELECTOR, "[class=result] button").text


def click_answer(num):
    print(f"clicking {num} as the fake gold")
    driver.find_element(By.CSS_SELECTOR, f"button[id='coin_{num}']").click()


def output_weightings_list():
    weights = driver.find_elements(By.CSS_SELECTOR, ".game-info ol li")
    for i in weights:
        print(i.text)


def print_alert_text():
    print(driver.switch_to.alert.text)


def dismiss_alert():
    driver.switch_to.alert.dismiss()


def set_up():
    driver.get("http://sdetchallenge.fetch.com/")


def tear_down():
    driver.quit()