from masterQA.fixtures.base_case import BaseCase
from masterQA.data.settings import environment as env


class MyTestClass(BaseCase):

    def test_anything(self):
        # Write your code here. Example:
        self.Open(env.URL)
        self.Click('//a[contains(text(),"Screener")]')
        self.Minimize_Screen()

    def test_anything2(self):
        # Write your code here. Example:
        self.Open(env.URL)
        self.Click("//a[contains(text(),'News')]")
        self.Scroll_Into_View("//a[contains(text(),'Do not sell my personal information')]")
        self.Scroll_Into_View("//a[contains(text(),'Screener')]")
        self.Select_by_index(1, "//select[@id='newsView']")
        self.Click("//a[contains(text(),'Crypto')]")
