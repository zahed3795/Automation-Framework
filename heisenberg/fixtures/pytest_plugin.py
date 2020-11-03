# -*- coding: utf-8 -*-
""" This is the pytest configuration file """

import pytest


@pytest.fixture()
def sb(request):
    """ As a pytest fixture.
        Usage example: "def test_one(sb):"
        You'll need to use this for tests that use other pytest fixtures. """
    from heisenberg import Base

    class BaseClass(Base):

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


