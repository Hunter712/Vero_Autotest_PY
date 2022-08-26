import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


profile_tabs = ["filter-featured", "filter-person", "filter-photo", "filter-video",
                "filter-link", "filter-music", "filter-movie", "filter-book",
                "filter-place", "filter-application", "filter-game"]

vero_link = "https://vero.co/ayman"


class VeroWebAutomate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/fedorchenkovlad/Downloads/chromedriver")

    def test_profile_navigating(self):
        driver = self.driver
        driver.get(vero_link)
        self.assertIn("Ayman Hariri on VERO™", driver.title)
        for tab in profile_tabs:            # Navigating through tabs in profile
            elem = driver.find_element(By.ID, tab)
            elem.click()
            time.sleep(2)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
