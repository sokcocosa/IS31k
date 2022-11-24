import unittest
import Coder_and_decoder


class MyTestCase(unittest.TestCase):
    def test_1(self):
        res = Coder_and_decoder.encode("OOOO")
        self.assertEqual(res, "34343434")

    def test_2(self):
        res = Coder_and_decoder.decode("34343434")
        self.assertEqual(res, "OOOO")




if __name__ == '__main__':
    unittest.main()
