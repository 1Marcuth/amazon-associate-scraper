from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pydantic import validate_call
from selenium import webdriver
from typing import Optional
import time
import json

DEFAULT_ORIGIN_URL = "https://amazon.com.br/"

driver_manager = ChromeDriverManager()

class AmazonAffiliate:
    @validate_call
    def __init__(
        self,
        cookies_file_path: str,
        origin_url: str = DEFAULT_ORIGIN_URL,
        webdriver_file_path: Optional[str] = driver_manager.install(),
        headless = True
    ) -> None:
        with open(cookies_file_path, "r+") as file:
            cookies = json.load(file)

        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless")

        service = Service(executable_path = webdriver_file_path)

        self._driver = webdriver.Chrome(
            options = options,
            service = service
        )

        self._driver.get(origin_url)

        self._driver.get_log

        for cookie in cookies:
            self._driver.add_cookie(cookie)

    @validate_call
    def create_affiliate_url(self, original_url: str) -> str:
        self._driver.get(original_url)

        self._driver.implicitly_wait(10)

        link_creator_element = self._driver.find_element(By.CSS_SELECTOR, "#amzn-ss-text-link a")
        link_creator_element.click()

        time.sleep(3)

        created_link_element = self._driver.find_element(By.CSS_SELECTOR, "#amzn-ss-text-shortlink-textarea")
        created_link = created_link_element.get_attribute("value")

        return created_link

    def close(self) -> None:
        self._driver.close()