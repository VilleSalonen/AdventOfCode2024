import unittest
from day3 import parse_multiplications

class TestDay3(unittest.TestCase):
    def test_part1_example(self):
        test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        result = parse_multiplications(test_input)
        self.assertEqual(result, 161, "Should be 2*4 + 5*5 + 11*8 + 8*5 = 161")

if __name__ == '__main__':
    unittest.main() 