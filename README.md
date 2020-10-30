# Super-Framework
This is a End to End Automation Framework

This is a Demo Test case. You just need to use `BaseCase` as gateway for End to End Automation world

```python
from masterQA.fixtures.base_case import BaseCase
from masterQA.common import encryption

# Test Information
USER_EMAIL = encryption.decrypt("$^*ENCRYPT=MhIVXBUeHGcxJV8=?&#$")
USER_PASSWORD = encryption.decrypt("$^*ENCRYPT=ZWIjSx5uEhVYGwUQ?&#$")


class MyTestClass(BaseCase):

    def test_anything(self):
        # Write your code here. Example:
        self.Open('https://finviz.com/')
        self.set_window_size(1400, 800)
        self.Get_page_title() == "FINVIZ.com - Stock Screener"
        self.Click("//a[contains(text(),'Login')]")
        self.Clear_Textbox("//input[@name='email']")
        self.Send_Text("//input[@name='email']", USER_EMAIL)
        self.Clear_Textbox("//input[@name='password']")
        self.Send_Text("//input[@name='password']", USER_PASSWORD)
        self.Submit("//input[@value='Log in']")
```

For Data encrypt and decrypt, you can go to `masterQA/common/unobfuscate` and need to run `main` for encrypts data also do not forget to add```from masterQA.common import encryption``` as import where you want to use it. As example go to `Demo_web_test/home_page.py`
```
Enter obfuscated/encrypted string: (CTRL-C to exit):
(Type data inside)

Here is the unobfuscated string/password:
$^*ENCRYPT=XBVURTE+KU0nQEMG?&#$

Enter obfuscated/encrypted string: (CTRL-C to exit):

Inside a test, use the following to decrypt it:

    from masterQA.common import encryption
    encryption.decrypt("$^*ENCRYPT=YEJUUS5TRTEW?&#$")

```


# List of Keyword and How to Use it

```python
from masterQA.fixtures.base_case import BaseCase


class MyTestClass(BaseCase):

    def test_anything(self):
        # Write your code here. Example:
        # This Function Will Maximize Windows
        self.Full_Screen()
        # This Function Will Minimize Windows
        self.Minimize_Screen()
        # This Function Will Press ENTER Key From Keyboard
        self.Press_Enter()
        # This Function Will Scroll Element Into View
        self.Scroll_Into_View()
        # This Function Will Help you to Submit
        self.Submit("locator", locatorType= "Can be none if it is XPATH, CSS, Name and LinkText")
        # This Function Will Help you to Click
        self.Click("locator", locatorType= "Can be none if it is XPATH, CSS, Name and LinkText")
        # This Function Will set windows size
        self.set_window_size(1200, 1200)
```


