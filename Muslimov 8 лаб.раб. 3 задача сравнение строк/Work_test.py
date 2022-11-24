import unittest
import Work


class MyTestCase(unittest.TestCase):
    def test_1(self):
        str1 = "абвгабвг"
        str2 = "аб"
        res = Work.worked(str1, str2)
        self.assertEqual(res, "Вывод: 2")

    def test_1(self):
        str1 = "стстсап"
        str2 = "стс"
        res = Work.worked(str1, str2)
        self.assertEqual(res, "Вывод: 2")




if __name__ == '__main__':
    unittest.main()
