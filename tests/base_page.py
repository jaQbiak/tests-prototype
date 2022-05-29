class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def get_title_of_page(self):
        """ This metod returns title of the current page """
        return self._driver.title
