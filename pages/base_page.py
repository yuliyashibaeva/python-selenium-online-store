from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, link):
        self.browser.get(link)

    def is_element_present(self, how, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
