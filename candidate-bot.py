from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from interval_timer import IntervalTimer


def wait_and_click(driver, by, value):
    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((by, value)))
    print(element)
    element.click()


def find_element(driver, by, value):
    found_element = driver.find_element(by, value)
    # print(found_element)
    # return found_element


def wait_for_url(driver, url):
    WebDriverWait(driver, 30).until(EC.url_to_be(url))


def handle_welcome_page(driver) -> bool:
    wait_and_click(driver, By.ID, "get-started-button")
    wait_for_url(driver, "http://localhost:4200/candidate/onboarding")
    if driver.current_url == "http://localhost:4200/candidate/onboarding":
        print("Welcome page passed ✅")
        return True
    else:
        print("Welcome page failed ❌")
        return False
    # return True if driver.current_url == "http://localhost:4200/candidate/onboarding" else False


def handle_candidate_login(driver, username) -> bool:
    driver.find_element(By.NAME, "login_field_value").send_keys(username)
    wait_and_click(driver, By.ID, "login-button")
    driver.implicitly_wait(20)
    # found_element = driver.find_element(By.ID, "login-error")
    # element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "login-error")))

    # print(found_element)

    # if found_element:
    #
    #     print("Candidate login failed ❌")
    #     # driver.quit()
    #
    # else:
    #     print("Candidate login passed ✅")
    # return True if find_element(driver, By.ID, "candidate-info") else False


def handle_read_instruction(driver):
    wait_and_click(driver, By.ID, "next-button")

    # return


def handle_start_exam(driver):
    wait_and_click(driver, By.ID, "start-exam")


def handle_end_exam(driver):
    print("end exam handler")


def handle_next_question(driver):
    for interval in IntervalTimer(5):
        wait_and_click(driver, By.ID, "next-question")
    print("next question handler")


def handle_previous_question(driver):
    wait_and_click(driver, By.ID, "previous-question")
    print("previous question handler")


def next_section_handler(driver):
    print("next section handler")


def main():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get("http://localhost:4200/candidate/welcome")
    handle_welcome_page(firefox_driver)
    handle_candidate_login(firefox_driver, "jamb@jamb.gov.ng12769")
    time.sleep(30)
    handle_read_instruction(firefox_driver)
    time.sleep(30)
    handle_start_exam(firefox_driver)
    time.sleep(5)
    handle_next_question(firefox_driver)
    handle_end_exam(firefox_driver)


#  if the script is the main program being executed
if __name__ == '__main__':
    main()
