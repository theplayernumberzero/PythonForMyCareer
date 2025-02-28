import unittest
import demo

#for unittest in terminal go project directory
#than write "python3 -m unittest file_name.py"
class TestDemo(unittest.TestCase):
    #this method is one test
    def test_add(self):
        self.assertEqual(demo.add(2,2), 4)
        self.assertEqual(demo.add(3,8), 11)
        self.assertEqual(demo.add(12,2), 14)

    def test_sub(self):
        self.assertEqual(demo.sub(10, 3), 7)
        self.assertEqual(demo.sub(19, 13), 6)

#aşağıdaki kod sayesinde "python3 file_name.py" yazman yeterli
if __name__ == "__main__":
    unittest.main()