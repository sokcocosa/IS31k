import unittest
import Square_eduaton


class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = 2
        b = -5
        c = 2
        res = Square_eduaton.square_ed(a, b, c)
        self.assertEqual(res, "x1 = 2.0  ;  x2 = 0.5")

    def test_2(self):
        a = 3
        b = 2
        c = 5
        res = Square_eduaton.square_ed(a, b, c)
        self.assertEqual(res, "Случай комплексных чисел")

    def test_3(self):
        a = 3
        b = -12
        c = 0
        res = Square_eduaton.square_ed(a, b, c)
        self.assertEqual(res, "x1 = 4.0  ;  x2 = 0.0")

    def test_4(self):
        a = 0
        b = 0
        c = 10
        res = Square_eduaton.square_ed(a, b, c)
        self.assertEqual(res, "Неразрешимое уравнение")

    def test_5(self):
        a = 0
        b = 0
        c = 0
        res = Square_eduaton.square_ed(a, b, c)
        self.assertEqual(res, "Неразрешимое уравнение")

    def test_6(self):
        a = 0
        b = 5
        c = 17
        res = Square_eduaton.square_ed(a, b, c)
        self.assertEqual(res, "Неквадратное уравнение")

    def test_7(self):
        a = 9
        b = 0
        c = 0
        res = Square_eduaton.square_ed(a, b, c)
        self.assertEqual(res, "x1 = x2 = 0")



if __name__ == '__main__':
    unittest.main()
