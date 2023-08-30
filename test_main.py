from main import div 
from main import umn 
import unittest2 as ut

class testcase1(ut.TestCase):
    def test1(self):
        self.assertEqual(div(20,2),10,'div 20/2')
    def test2(self):
        self.assertEqual(div(20,-5),-4,'div 20/-4')
    def test3(self):
        self.assertNotEqual(div(20,0),ZeroDivisionError,'Ошибка деления на ноль')
    def test4(self):
        self.assertEqual(umn(20,0),0,'umn 20*0')
    def test5(self):
        self.assertNotEqual(umn(100,3),300,'umn 100*3')
        
ut.main()