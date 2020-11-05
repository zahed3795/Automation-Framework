# Super-Framework
This is a End to End Automation Framework


<h2>Need to run installation.bat in CMD or terminal for installation and this step is must: 🚀</h2>

[installation.bat](https://github.com/zahed3795/Super-Framework/blob/master/installation.bat)

This is a Demo Test case. You just need to use `Base` as gateway for End to End Automation world

```python
from framework.fixtures.base_case2 import Base
from framework.crypt import encryption

# Test Information
USER_EMAIL = encryption.decrypt("$^*ENCRYPT=MhIVXBUeHGcxJV8=?&#$")
USER_PASSWORD = encryption.decrypt("$^*ENCRYPT=ZWIjSx5uEhVYGwUQ?&#$")


class MyTestClass(Base):

    def test_one(self):
        # Write your code here. Example:
        self.Open('https://finviz.com/')
        self.set_window_size(1400, 800)
        assert self.Get_page_title() == "FINVIZ.com - Stock Screener"
        self.Click("//a[contains(text(),'Login')]")
        self.Clear_Textbox("//input[@name='email']")
        self.Send_Text("//input[@name='email']", USER_EMAIL)
        self.Clear_Textbox("//input[@name='password']")
        self.Send_Text("//input[@name='password']", USER_PASSWORD)
        self.Submit("//input[@value='Log in']")
```

* To list all commands: ``zahed --help``
### Options

*For Usage options commands:
``zahed options``

### Install
* Examples:
``zahed install chrome latest``
``zahed install firefox latest``
``zahed install edge latest``
``zahed install opera latest``
``zahed install ie latest``

### encrypt / obfuscate

* Usage:
``zahed encrypt``  OR  ``zahed obfuscate``

### decrypt / unobfuscate

* Usage:
``zahed decrypt``  OR  ``zahed unobfuscate``

### download

* Usage:
``zahed download [ITEM]``
        (Options: server)

* Example:
``zahed download server``

### grid-hub

* Usage:
``zahed grid-hub {start|stop|restart} [OPTIONS]``

* Options:
``-v``, ``--verbose``  (Increases verbosity of logging output.)
``--timeout=TIMEOUT``  (Close idle browser windows after TIMEOUT seconds.)

### grid-node

* Usage:
``zahed grid-node {start|stop|restart} [OPTIONS]``

* Options:
``--hub=HUB_IP`` (The Grid Hub IP Address to connect to.) (Default: ``127.0.0.1``)
``-v``, ``--verbose``  (Increases verbosity of logging output.)



For Data encrypt and decrypt, you can run `zahed encrypt` and `zahed decrypt` from console or cmd
```
Enter obfuscated/encrypted string: (CTRL-C to exit):
(Type data inside)

Here is the unobfuscated string/password:
$^*ENCRYPT=XBVURTE+KU0nQEMG?&#$

Enter obfuscated/encrypted string: (CTRL-C to exit):

Inside a test, use the following to decrypt it:

    from masterQA.crypt import encryption
    encryption.decrypt("$^*ENCRYPT=YEJUUS5TRTEW?&#$")

```


### List of Keyword and How to Use it

```python
from framework.fixtures.base_case2 import Base


class MyTestClass(Base):

    def test_anything(self):
        # Write your code here. Example:
        # This Function Will Maximize Windows
        self.Full_Screen()
        # This Function Will Minimize Windows
        self.Minimize_Screen()
        # This Function Will Press ENTER Key From Keyboard
        self.Press_Enter()
        # This Function Will Help you to click to an web element
        self.Click("locator", locatorType= "Can be none if it is XPATH, CSS, Name and LinkText")
        # This Function Will Help you to Submit
        self.Submit("locator", locatorType= "Can be none if it is XPATH, CSS, Name and LinkText")
        # This Function Will Help you to Click
        self.Click("locator", locatorType= "Can be none if it is XPATH, CSS, Name and LinkText")
        # This Function Will set windows size
        self.set_window_size(1200, 1200)
        # Print user agent in log
        print(self.get_user_agent())
        # It will take you to the browser that you launch at the beginning
        self.switch_to_default_window()  
        # Use for get system navigator language
        print(self.get_locale_code())
        # Useful for get page title
        print(self.Get_page_title())
        # Useful for get current page URL
        print(self.Get_current_url())
        # Refresh page and can mention delay if you want
        self.Refresh_page(delay=5) or self.Refresh_page()
        # Use in for scroll an element into view of the screen        
        self.Scroll_Into_View('locator')
        # Use it for select a dropdown by index
        self.Select_by_index(1, 'locator')
        # Use it for select a dropdown by value
        self.Select_by_value('Type value', 'locator')
        # Use it for select a dropdown by visible text
        self.Select_by_visible_text('Type visible text', 'locator')
        # Useful if you want to press Enter key from keyboard        
        self.Press_Enter()
        # This is ActionChains class and need to implement Action class methods
        self.KeyBoard().perform()
        # Useful for double click into element
        self.Double_Click('locator')
        # Use explicit wait over a element or mention time 
        self.web_driver_wait('locator', delay=2) or self.web_driver_wait('locator')
        # Works for submit somethings in page        
        self.Submit('locator')
        # It will enter text in a text box
        self.Send_Text('Text', 'locator')
        # It will clear text or a textbox
        self.Clear_Textbox('Text', 'locator')
        # Useful for replacing exiting text form textbox
        self.Replace_existing_text('Text', 'locator')
        # print page source in html format
        print(self.get_beautiful_soup())
        #Get all unique links in the html of the page source.
        print(self.get_unique_links())
        # This function print all unique links with status codes
        self.print_unique_links_with_status_codes()
        # helps download file. Mention location or by default it will download testing folder
        self.Download_file('URL') or self.Download_file('URl','my location')
        # helps download data. Mentioning `data name` is must and Mention location or by default it will download testing folder
        self.save_data_as('myfile.txt', 'my location')
        # helps download file. Mentioning `file name` is must and Mention location or by default it will download testing folder
        self.save_file_as('myfile', 'my location')
        # You can save unique links by using this function
        url_link = self.get_unique_links()
        self.save_data_as(url_link, 'myfile.txt')
```

###  This is a Demo Test case. You just need to use ```StringBase``` as gateway for string world
```python
from framework.core.string import StringBase
from framework.fixtures.base_case2 import Base

class MyTestClass(Base, StringBase):

    def test_anything(self):
        # Write your code here. Example:
        
        # Convert string into lower case
        self.convert_to_lower_case('<----ABCD---->')
        # Convert string into upper case
        self.convert_to_upper_case('<----abcd---->')
        # Get line count from string
        self.get_line_count('\n1..a,\n2..a,\n3..a,\n4..a')  
        # Split lines from string as parameter need argument
        self.split_to_lines("\nfirst \n2nd \n3rd", 2)  
        # Returns a list of all non-overlapping matches in the given string
        self.get_regexp_matches('the string','xxx') 
        #Replaces ``search_for`` in the given ``string`` with ``replace_with`
        self.replace_string('Hello_world!','In_god_we_trust')
```


