import unittest
from day3 import parse_multiplications

class TestDay3(unittest.TestCase):
    def test_part1_example(self):
        test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        result = parse_multiplications(test_input)
        self.assertEqual(result, 161, "Should be 2*4 + 5*5 + 11*8 + 8*5 = 161")

    def test_part1_invalid_formats(self):
        # Test various invalid formats
        invalid_inputs = [
            "mul(4*",
            "mul(6,9!",
            "?(12,34)",
            "mul ( 2 , 4 )",
            "mul[3,4]",
            "mul{5,6}",
            "mul(1000,1)",  # Numbers > 999
            "mul(-1,5)",    # Negative numbers
            "multiply(3,4)" # Wrong keyword
        ]
        for invalid in invalid_inputs:
            result = parse_multiplications(invalid)
            self.assertEqual(result, 0, f"Invalid format '{invalid}' should return 0")

    def test_part1_valid_formats(self):
        # Test valid formats
        test_cases = [
            ("mul(1,1)", 1),
            ("mul(10,10)", 100),
            ("mul(999,999)", 998001),
            ("mul(5,7)mul(2,3)", 17),  # Multiple valid multiplications
            ("amul(5,7)", 0),          # Part of another word
            ("mul(5,7)a", 35),         # Trailing character
        ]
        for test_input, expected in test_cases:
            result = parse_multiplications(test_input)
            self.assertEqual(result, expected, f"Failed for input '{test_input}'")

    def test_part2_example(self):
        test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))"
        result = parse_multiplications(test_input, handle_conditions=True)
        self.assertEqual(result, 48, "Should be 2*4 + 8*5 = 48")

    def test_part2_conditions(self):
        test_cases = [
            ("mul(2,3)don't()mul(4,5)do()mul(6,7)", 2*3 + 6*7),  # Basic enable/disable
            ("don't()mul(2,3)mul(4,5)", 0),                       # Start disabled
            ("do()mul(2,3)mul(4,5)", 2*3 + 4*5),                 # Start enabled explicitly
            ("mul(2,3)do()don't()mul(4,5)do()mul(6,7)", 2*3 + 6*7),  # Multiple toggles
            ("mul(2,3)don't()mul(4,5)don't()mul(6,7)", 2*3),     # Multiple disables
            ("mul(2,3)do()mul(4,5)do()mul(6,7)", 2*3 + 4*5 + 6*7),  # Multiple enables
        ]
        for test_input, expected in test_cases:
            result = parse_multiplications(test_input, handle_conditions=True)
            self.assertEqual(result, expected, f"Failed for input '{test_input}'")

if __name__ == '__main__':
    unittest.main() 