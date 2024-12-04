def is_safe_report(levels):
    if len(levels) <= 1:
        return False
        
    # Check first two numbers to determine if increasing or decreasing
    increasing = levels[1] > levels[0]
    
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        
        # If increasing, diff should be positive
        if increasing and diff <= 0:
            return False
        # If decreasing, diff should be negative    
        if not increasing and diff >= 0:
            return False
            
        # Check if difference is between 1 and 3 (inclusive)
        if abs(diff) < 1 or abs(diff) > 3:
            return False
            
    return True

def is_safe_with_dampener(levels):
    # First check if it's safe without removing any level
    if is_safe_report(levels):
        return True
        
    # Try removing each level one at a time
    for i in range(len(levels)):
        # Create new list without the current level
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe_report(dampened_levels):
            return True
            
    return False

def solve_part1():
    safe_count = 0
    
    with open('day2_input.txt', 'r') as f:
        for line in f:
            # Convert line of numbers to list of integers
            levels = [int(x) for x in line.strip().split()]
            if is_safe_report(levels):
                safe_count += 1
                
    return safe_count

def solve_part2():
    safe_count = 0
    
    with open('day2_input.txt', 'r') as f:
        for line in f:
            # Convert line of numbers to list of integers
            levels = [int(x) for x in line.strip().split()]
            if is_safe_with_dampener(levels):
                safe_count += 1
                
    return safe_count

if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1 - Number of safe reports: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2 - Number of safe reports with dampener: {result2}") 