import unittest
from day3 import parse_multiplications

class TestDay3(unittest.TestCase):
    def test_part1_example(self):
        test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        result = parse_multiplications(test_input)
        self.assertEqual(result, 161, "Should be 2*4 + 5*5 + 11*8 + 8*5 = 161")
    
    def test_part1_solution(self):
        with open('src/day3_input.txt', 'r') as file:
            puzzle_input = file.read()
        result = parse_multiplications(puzzle_input)
        print(f"\nPart 1 Solution: {result}")
        self.assertEqual(result, 175015740, "Part 1 solution")

if __name__ == '__main__':
    unittest.main() 