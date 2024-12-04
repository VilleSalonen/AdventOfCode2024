import re

def parse_multiplications(text, handle_conditions=False):
    if not handle_conditions:
        # Part 1: Simple multiplication parsing
        pattern = r'\bmul\(\d{1,3},\d{1,3}\)'
        matches = re.findall(pattern, text)
        
        total = 0
        for match in matches:
            x, y = map(int, match[4:-1].split(','))
            total += x * y
            
        return total
    
    # Part 2: Handle do() and don't() conditions
    total = 0
    enabled = True  # Multiplications are enabled by default
    
    # Find all instructions in order of appearance
    mul_pattern = r'\bmul\(\d{1,3},\d{1,3}\)'
    do_pattern = r'\bdo\(\)'
    dont_pattern = r'\bdon\'t\(\)'
    
    # Get all matches with their positions
    all_matches = []
    
    for match in re.finditer(mul_pattern, text):
        all_matches.append(('mul', match.start(), match.group()))
    for match in re.finditer(do_pattern, text):
        all_matches.append(('do', match.start(), match.group()))
    for match in re.finditer(dont_pattern, text):
        all_matches.append(('dont', match.start(), match.group()))
    
    # Sort matches by position to process them in order
    all_matches.sort(key=lambda x: x[1])
    
    # Process instructions in order
    for type, _, instruction in all_matches:
        if type == 'do':
            enabled = True
        elif type == 'dont':
            enabled = False
        elif type == 'mul' and enabled:
            # Extract and multiply numbers
            x, y = map(int, instruction[4:-1].split(','))
            total += x * y
            
    return total

def solve_part1():
    total = 0
    with open('day3_input.txt', 'r') as f:
        for line in f:
            total += parse_multiplications(line.strip())
    return total

def solve_part2():
    total = 0
    with open('day3_input.txt', 'r') as f:
        for line in f:
            total += parse_multiplications(line.strip(), handle_conditions=True)
    return total

if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1 - Sum of all multiplication results: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2 - Sum of enabled multiplication results: {result2}") 