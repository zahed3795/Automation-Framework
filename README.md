# Super-Framework
This is a End to End Automation Framework

This is a Demo Test case. You just need to use `BaseCase` as gateway for End to End Automation world

```
from masterQA.fixtures.base_case import BaseCase


class MyTestClass(BaseCase):

    def test_anything(self):
        # Write your code here. Example:
        self.open('https://finviz.com/')
        self.full_screen()
        self.Click('//a[contains(text(),"Screener")]', 'xpath')
```

For Data encrypt, you can use `sbase encrypt ` and `sbase decrypt` for decrypt Data in cmd or run `cryption.bat` file from advance file.
Example
Enter password to obfuscate: (CTRL-C to exit)
Password:
```
Enter password to obfuscate: (CTRL-C to exit)
Password:
Here is the obfuscated password:
$^*ENCRYPT=YEJUUS5TRTEW?&#$

Inside a test, use the following to decrypt it:

    from seleniumbase import encryption
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
        
```

