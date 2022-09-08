import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

profile_tabs = ["filter-all", "filter-featured", "filter-person", "filter-photo", "filter-video",
                "filter-link", "filter-music", "filter-movie", "filter-book",
                "filter-place", "filter-application", "filter-game"]

vero_link = "https://vero.co/krutko"
path_to_chromedriver = "/Users/fedorchenkovlad/Downloads/chromedriver"
waiting_time_ = 1

def check_exists_by(driver):
    try:
        driver.find_element(By.LINK_TEXT, 'SHOW MORE')
    except NoSuchElementException:
        return False
    return True


def navigate_on_tabs(driver):
    for tab in profile_tabs:  # Navigating through tabs in profile
        elem = driver.find_element(By.ID, tab)
        elem.click()
        time.sleep(waiting_time_)
        scrolling_on_page(driver)   # Call function to scroll the page


def scrolling_on_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll to the bottom of the page
    time.sleep(waiting_time_)

    if check_exists_by(driver):
        elem = driver.find_element(By.LINK_TEXT, 'SHOW MORE')
        elem.click()
        time.sleep(waiting_time_)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll to the bottom of the page

    time.sleep(waiting_time_)
    driver.execute_script("window.scrollTo(0,0)")  # scroll to the top of the page
    time.sleep(waiting_time_)


class VeroWebAutomate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path_to_chromedriver)

    def test_profile_navigating(self):
        driver = self.driver
        driver.get(vero_link)

        self.assertIn("Julia Krutko on VERO™", driver.title)  # An assertion to confirm that title has “Python” word in it
        navigate_on_tabs(driver)    # Call function to open all tabs in profile
        self.assertNotIn("No results found.", driver.page_source)  # Results are found

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
