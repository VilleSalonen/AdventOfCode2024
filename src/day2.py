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

def solve_part1():
    safe_count = 0
    
    with open('day2_input.txt', 'r') as f:
        for line in f:
            # Convert line of numbers to list of integers
            levels = [int(x) for x in line.strip().split()]
            if is_safe_report(levels):
                safe_count += 1
                
    return safe_count

if __name__ == "__main__":
    result = solve_part1()
    print(f"Number of safe reports: {result}") 