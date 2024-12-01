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

def solve_part2(left_list, right_list):
    """
    Calculate similarity score by:
    1. Counting frequency of each number in right list
    2. For each number in left list, multiply it by its frequency in right list
    3. Sum all products
    """
    # Count frequency of numbers in right list
    right_freq = {}
    for num in right_list:
        right_freq[num] = right_freq.get(num, 0) + 1
    
    # Calculate similarity score
    similarity_score = sum(num * right_freq.get(num, 0) for num in left_list)
    return similarity_score

def main():
    left_list, right_list = read_input('day1_input.txt')
    
    # Part 1
    result1 = solve_part1(left_list, right_list)
    print(f"Total distance between lists: {result1}")
    
    # Part 2
    result2 = solve_part2(left_list, right_list)
    print(f"Similarity score: {result2}")

if __name__ == '__main__':
    main() 