from selenium import webdriver
from abc import ABCMeta, abstractmethod
import os
import itertools
import time


def get_options():
    options = webdriver.ChromeOptions()
    options.binary_location = "/opt/python/bin/headless-chromium"
    options.add_argument("--headless")
    options.add_argument("--homedir=/tmp")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    return options


class ServerlessChrome(webdriver.Chrome):
    def __init__(self):
        kw = {'executable_path': "/opt/python/bin/chromedriver", 'options': get_options(
        )} if os.environ.get("STAGE", "local") != "local" else {}
        super().__init__(**kw)

    def wait_element(self, xpath, timeout=None):
        start_time = time.time()
        for _ in itertools.count():
            if len(self.xpaths(xpath)):
                break
            if timeout and time.time() > start_time + timeout:
                raise Exception(
                    ' '.join(["timeoutException. xpath:", xpath,  "is not found"]))
            time.sleep(0.1)


ServerlessChrome.xpaths = ServerlessChrome.find_elements_by_xpath
ServerlessChrome.xpath = ServerlessChrome.find_element_by_xpath


class KabuChrome(ServerlessChrome, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.login()

    @abstractmethod
    def login(self):
        pass

    def test(self):
        result = {
            'login': self.test_login(),
            'get_current_asset': self.test_get_current_asset(),
        }
        self.quit()
        return result

    @abstractmethod
    def test_login(self):
        pass

    @abstractmethod
    def test_get_current_asset(self):
        pass


def test_chrome():
    chrome = ServerlessChrome()
    try:
        chrome.get("https://www.google.com/")
        assert len(chrome.xpaths("//input")) > 0
        title = chrome.title
        assert title == "Google"
        chrome.wait_element("//img")
        return title
    except Exception:
        raise
    finally:
        chrome.quit()
