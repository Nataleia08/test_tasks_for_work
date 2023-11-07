import unittest
from function import Shape, ShapeName

class TestShape(unittest.TestCase):
    def test_squre(self):
        shape1 = Shape(1, 1, "Square")
        result1 = shape1.area_and_perimeter_square(2)
        self.assertEqual(result1, (8, 4))
    
    def test_rectangle(self):
        shape2 = Shape(1,1,"Rectangle")
        result2 = shape2.area_and_perimeter_rectangle(2,2)
        self.assertEqual(result2, (4, 1))

    def test_circle(self):
        shape3 = Shape(1, 1, "Circle")
        result3 = shape3.area_and_perimeter_circle(2)
        self.assertEqual(result3, (12.566370614359172, 12.566370614359172))



if __name__ == '__main__':
    unittest.main()

