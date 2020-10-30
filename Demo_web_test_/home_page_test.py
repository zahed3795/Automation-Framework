from masterQA.fixtures.base_case import BaseCase
from masterQA.data.settings import environment as env
from masterQA.common import encryption

# Test Information
USER_EMAIL = encryption.decrypt("$^*ENCRYPT=MhIVXBUeHGcxJV8=?&#$")
USER_PASSWORD = encryption.decrypt("$^*ENCRYPT=ZWIjSx5uEhVYGwUQ?&#$")


class MyTestClass(BaseCase):

    def test_anything(self):
        # Write your code here. Example:
        self.Open(env.URL)
        self.set_window_size(1300, 800)
        self.Get_page_title() == "FINVIZ.com - Stock Screener"
        self.Click("//a[contains(text(),'Login')]")
        self.Clear_Textbox("//input[@name='email']")
        self.Send_Text("//input[@name='email']", USER_EMAIL)
        self.Clear_Textbox("//input[@name='password']")
        self.Send_Text("//input[@name='password']", USER_PASSWORD)
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
