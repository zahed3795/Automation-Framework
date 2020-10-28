# -*- coding: utf-8 -*-
""" This is the pytest configuration file """

import colorama
import pytest
import sys


@pytest.fixture()
def sb(request):
    """ SeleniumBase as a pytest fixture.
        Usage example: "def test_one(sb):"
        You'll need to use this for tests that use other pytest fixtures. """
    from masterQA import BaseCase

    class BaseClass(BaseCase):

        def setUp(self):
            super(BaseClass, self).setUp()

        def tearDown(self):
            self.save_teardown_screenshot()
            super(BaseClass, self).tearDown()

        def base_method(self):
            pass

    if request.cls:
        request.cls.sb = BaseClass("base_method")
        request.cls.sb.setUp()
        request.cls.sb._needs_tearDown = True
        request.cls.sb
        yield request.cls.sb
        if request.cls.sb._needs_tearDown:
            request.cls.sb.tearDown()
            request.cls.sb._needs_tearDown = False
    else:
        sb = BaseClass("base_method")
        sb.setUp()
        sb._needs_tearDown = True
        yield sb
        if sb._needs_tearDown:
            sb.tearDown()
            sb._needs_tearDown = False


