# -*- coding: utf-8 -*-
import pytest

from .testing import get_connection_string


@pytest.fixture
def connection_string():
    """Returns a connection string"""
    return get_connection_string()
