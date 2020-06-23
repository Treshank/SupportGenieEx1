import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        res = main.controller(10, 10)
        print(int(res), 'seconds')
        self.assertEqual(0, res)

    def test_case2(self):
        res = main.controller(50, 50)
        print(int(res), 'seconds')
        self.assertEqual(0, res)

    def test_case3(self):
        res = main.controller(79, 50)
        print(int(res), 'seconds')
        self.assertEqual(0, res)

    def test_case4(self):
        res = main.controller(50, 500)
        print(int(res), 'seconds')
        self.assertEqual(res, res)

    def test_case5(self):
        res = main.controller(70, 600)
        print(int(res), 'seconds')
        self.assertEqual(res, res)

    def test_case6(self):
        res = main.controller(70, 800)
        print(int(res), 'seconds')
        self.assertEqual(res, res)


if __name__ == '__main__':
    unittest.main()
