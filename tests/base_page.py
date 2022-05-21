class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def _get_title_of_page(self):
        return self._driver.title
