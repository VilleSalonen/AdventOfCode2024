def read_input(filename):
    """Read the input file and return two separate lists"""
    left_list = []
    right_list = []
    with open(filename) as f:
        for line in f:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def solve_part1(left_list, right_list):
    """
    Find total distance between sorted lists by:
    1. Sorting both lists independently
    2. Finding absolute difference between corresponding elements
    3. Summing all differences
    """
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total_distance

def main():
    left_list, right_list = read_input('day1_input.txt')
    
    # Part 1
    result = solve_part1(left_list, right_list)
    print(f"Total distance between lists: {result}")

if __name__ == '__main__':
    main() 