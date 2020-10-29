from masterQA.fixtures.base_case import BaseCase
from masterQA.data.settings import environment as env


class MyTestClass(BaseCase):

    def test_anything(self):
        # Write your code here. Example:
        self.Open(env.URL)
        self.set_window_size(1200, 1200)
        self.Get_page_title() == "FINVIZ.com - Stock Screener"
        self.Click("//a[contains(text(),'Login')]")
        self.Clear_Textbox("//input[@name='email']")
        self.Send_Text("//input[@name='email']", "zahed3795@icloud.com")
        self.Clear_Textbox("//input[@name='password']")
        self.Send_Text("//input[@name='password']", "Conan3795@")
        self.Submit("//input[@value='Log in']")
        self.Minimize_Screen()
        self.tearDown()

    def test_anything2(self):
        # Write your code here. Example:
        self.Open(env.URL)
        self.Click("//a[contains(text(),'News')]")
        self.Scroll_Into_View("//a[contains(text(),'Do not sell my personal information')]")
        self.Scroll_Into_View("//a[contains(text(),'Screener')]")
        self.Select_by_index(1, "//select[@id='newsView']")
        self.Click("//a[contains(text(),'Crypto')]")
        self.tearDown()
