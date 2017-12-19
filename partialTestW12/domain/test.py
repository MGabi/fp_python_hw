"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/19/2017 13:19
"""
from unittest import TestCase

from controller import Controller
from domain.entities.driver import Driver


class TestController(TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_Controller(self):
        self.assertEqual(self.controller.distanceFrom(Driver("abc",1,1), Driver("abc",1,1)), 0)