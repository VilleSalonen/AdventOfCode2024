import re

def parse_multiplications(text: str) -> int:
    # Find all potential mul(X,Y) patterns where X and Y are 1-3 digit numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(pattern, text)
    
    total = 0
    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        total += x * y
    
    return total
