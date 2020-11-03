def are_quotes_escaped(string):
    if (string.count("\\'") != string.count("'") or (
            string.count('\\"') != string.count('"'))):
        return True
    return False


def escape_quotes_if_needed(string):
    """
    re.escape() works differently in Python 3.7.0 than earlier versions:

    Python 3.6.5:
    >>> import re
    >>> re.escape('"')
    '\\"'

    Python 3.7.0:
    >>> import re
    >>> re.escape('"')
    '"'

    SeleniumBase needs quotes to be properly escaped for Javascript calls.
    """
    if are_quotes_escaped(string):
        if string.count("'") != string.count("\\'"):
            string = string.replace("'", "\\'")
        if string.count('"') != string.count('\\"'):
            string = string.replace('"', '\\"')
    return string
