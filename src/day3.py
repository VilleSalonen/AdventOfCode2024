def find_closing_parenthesis(text, start):
    """Find the matching closing parenthesis starting from position start"""
    count = 1
    i = start
    while i < len(text) and count > 0:
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
        i += 1
    return i - 1 if count == 0 else -1

def parse_instruction(text, pos):
    """Parse an instruction starting at pos, return (type, end_pos, numbers)"""
    if text[pos:pos+3] == 'mul':
        if pos > 0 and text[pos-1].isalpha():  # Skip if part of another word
            return None
        
        # Find the opening parenthesis
        p_start = pos + 3
        while p_start < len(text) and text[p_start] != '(':
            p_start += 1
        if p_start >= len(text):
            return None
            
        # Find closing parenthesis
        p_end = find_closing_parenthesis(text, p_start + 1)
        if p_end == -1:
            return None
            
        # Parse the numbers
        try:
            content = text[p_start+1:p_end]
            x, y = map(int, content.split(','))
            if 0 <= x <= 999 and 0 <= y <= 999:  # Validate number range
                return ('mul', p_end, (x, y))
        except:
            pass
        return None
        
    elif text[pos:pos+2] == 'do':
        if pos > 0 and text[pos-1].isalpha():  # Skip if part of another word
            return None
        if text[pos:pos+5] == 'do()':
            return ('do', pos+4, None)
        return None
        
    elif text[pos:pos+5] == "don't":
        if pos > 0 and text[pos-1].isalpha():  # Skip if part of another word
            return None
        if text[pos:pos+7] == "don't()":
            return ('dont', pos+6, None)
        return None
    
    return None

def parse_multiplications(text, handle_conditions=False):
    if not handle_conditions:
        # Part 1: Only handle multiplications
        total = 0
        pos = 0
        while pos < len(text):
            instruction = parse_instruction(text, pos)
            if instruction and instruction[0] == 'mul':
                x, y = instruction[2]
                total += x * y
            pos += 1
        return total
    
    # Part 2: Handle do() and don't() conditions
    total = 0
    enabled = True
    pos = 0
    
    while pos < len(text):
        instruction = parse_instruction(text, pos)
        if instruction:
            type, end_pos, numbers = instruction
            if type == 'do':
                enabled = True
            elif type == 'dont':
                enabled = False
            elif type == 'mul' and enabled:
                x, y = numbers
                total += x * y
            pos = end_pos
        pos += 1
        
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