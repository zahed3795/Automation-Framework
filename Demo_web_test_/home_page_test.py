from masterQA.fixtures.base_case import BaseCase
from masterQA.data.settings import environment as env


class MyTestClass(BaseCase):

    def test_anything(self):
        # Write your code here. Example:
        self.Open(env.URL)
        self.Click('//a[contains(text(),"Screener")]')

    def test_anything2(self):
        # Write your code here. Example:
        self.Open(env.URL)
        self.Click('//a[contains(text(),"Screener")]')

