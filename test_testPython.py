import unittest
import pytest
import testPython

def test_add():
    assert testPython.add(7,3) == 10
    assert testPython.add(7) == 9

def test_product():
    assert testPython.product(5,5) == 25
    assert testPython.product(5) == 10