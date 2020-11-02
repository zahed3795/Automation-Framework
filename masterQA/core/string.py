"""A test library for string manipulation and verification"""


def lower(string):
    return string.lower()


def upper(string):
    return string.upper()


def _convert_to_index(value, name):
    if value == '':
        return 0
    if value is None:
        return None
    return _convert_to_integer(value, name)


def _convert_to_integer(value, name):
    try:
        return int(value)
    except ValueError:
        raise ValueError("Cannot convert '%s' argument '%s' to an integer."
                         % (name, value))


class StringBase:

    def convert_to_lower_case(self, string):
        return lower("\n" + str(string))

    def convert_to_upper_case(self, string):
        return upper("\n" + str(string))

    def get_line_count(self, string):
        """Returns and logs the number of lines in the given string."""
        count = len(string.splitlines())
        return count

    def split_to_lines(self, string, start=0, end=None):
        """Splits the given string to lines"""
        start = _convert_to_index(start, 'start')
        end = _convert_to_index(end, 'end')
        lines = string.splitlines()[start:end]
        return lines

    def get_line(self, string, line_number):
        """Returns the specified line from the given ``string``."""
        line_number = _convert_to_integer(line_number, 'line_number')
        return string.splitlines()[line_number]
