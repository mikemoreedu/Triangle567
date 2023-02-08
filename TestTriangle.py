# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(10, 10, 12), 'Isosceles', '10,10,12 is an Isosceles triangle')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene', '1,2,3 is a Scalene triangle')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(4, -1, 3), 'InvalidInput', '4,-1,3 is an ivalid input')

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(5, 1, 12), 'NotATriangle', '5,1,12 is an not a triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

