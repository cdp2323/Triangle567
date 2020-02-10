import unittest

from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    def testEquilateralTriangleC(self):
        self.assertEqual(classifyTriangle(22, 22, 22), 'Equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(3333, 3333, 3333), 'Equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(11, 16, 13), 'Scalene')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(5, 5, 4), 'Isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(44, 66, 66), 'Isoceles')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-99, -99, -99), 'InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(322, 322, 0), 'InvalidInput')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(3, 1, 1), 'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(20, 50, 20), 'NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(233, 233, 499), 'NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()