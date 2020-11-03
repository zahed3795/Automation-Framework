# We are following Page Object Model and All the locator will be store here only

class HOMEPAGE:
    LOGIN_BUTTON = "//a[contains(text(),'Login')]"


class LOGIN_PAGE:
    USERNAME_BOX = "//input[@name='email']"
    PASSWORD_BOX = "//input[@name='password']"
    LOGIN_BUTTON = 'a.nav-link.sign-in'
