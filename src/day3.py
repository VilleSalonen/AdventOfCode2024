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

def parse_multiplications_with_conditions(text: str) -> int:
    # Find all control instructions and multiplications with their positions
    control_pattern = r'(?:do|don\'t)\(\)'
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    controls = [(m.group(0), m.start()) for m in re.finditer(control_pattern, text)]
    muls = [(int(m.group(1)), int(m.group(2)), m.start()) for m in re.finditer(mul_pattern, text)]
    
    total = 0
    # Start enabled by default
    enabled = True
    
    for x, y, mul_pos in muls:
        # Find the last control instruction before this multiplication
        last_control = None
        for control, control_pos in controls:
            if control_pos < mul_pos:
                last_control = control
            else:
                break
        
        # Update enabled state based on last control instruction
        if last_control == "don't()":
            enabled = False
        elif last_control == "do()":
            enabled = True
            
        if enabled:
            total += x * y
    
    return total
