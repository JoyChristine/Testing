import calc
import unittest


class Testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1,100),101)
        self.assertEqual(calc.subtract(33,19), 14)
        self.assertEqual(calc.multiply(2,4), 8)
        self.assertEqual(calc.divide(33,11), 3)
   
    

class TestRectangle(unittest.TestCase):
    def test_rectangle(self):
        rectangle = calc.Rectangle(2,3)
        self.assertEqual(rectangle.get_area(),6,"should be 6")


if__name__ = "__main__" 
unittest.main()



# import unittest
# import fractions
# # from mysum import Sum

# class TestSum(unittest.TestCase):
   
#     def test_list_int(self):
#         data = [1, 2, 3]
#         result = sum(data)
#         self.assertEqual(result,6)

#     def test_list_fraction(self):
#         data = [1/3, 2/5, 3/5]
#         result = sum(data)
#         self.assertEqual(result,1.3333333333333335)
# if__name__ = "__main__" 
# unittest.main()




