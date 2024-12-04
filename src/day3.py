import re

def parse_multiplications(text):
    # Pattern to match mul(X,Y) where X and Y are 1-3 digit numbers
    # \b ensures we match whole words (not part of other words)
    # \d{1,3} matches 1-3 digits
    pattern = r'\bmul\(\d{1,3},\d{1,3}\)'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    total = 0
    for match in matches:
        # Extract the numbers from mul(X,Y)
        x, y = map(int, match[4:-1].split(','))
        total += x * y
        
    return total

def solve_part1():
    total = 0
    
    with open('day3_input.txt', 'r') as f:
        for line in f:
            total += parse_multiplications(line.strip())
            
    return total

if __name__ == "__main__":
    result = solve_part1()
    print(f"Sum of all multiplication results: {result}") 