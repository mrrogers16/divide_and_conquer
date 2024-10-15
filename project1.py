import sys

def read_stocks(filename):

    prices = []

    # Read in specified file and return array of floats
    try:
        with open(filename, "r") as file:
            for line in file:
                # Strip any leading/trailing whitespace chars
                line = line.strip()
                # Skip empty lines
                if line == "":
                    continue
                # Convert line to float and append to price list
                try:
                    price = float(line)
                    prices.append(price)
                except ValueError:
                    print(
                        f"Error: The line '{line}' is not a valid number. Skipping this line."
                    )
                    continue

        # Return array of floats
        return prices

    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")
        exit(1)


def find_max_profit(prices):
    n = len(prices)
    if n < 2:
        return 0  # No profit can be made with less than 2 prices

    # Initialize differences array
    diff = []
    # Compute the differences between consecutive prices and append to diff array
    for i in range(n - 1):
        current_price = prices[i]
        next_price = prices[i + 1]
        difference = next_price - current_price
        diff.append(difference)

    max_profit = max_subarray(diff, 0, n - 2)

    if max_profit < 0:
        return 0
    else:
        return max_profit


def max_subarray(diff, low, high):
    # Base case: one element
    if low == high:
        return diff[low]

    # Find mid point
    mid = (low + high) // 2
    # Find max subarray sum in left half
    left_max = max_subarray(diff, low, mid)
    # Find max subarray sum in right half
    right_max = max_subarray(diff, mid + 1, high)
    # Find max subarray sum that crosses midpoint
    cross_max = max_crossing_subarray(diff, low, mid, high)

    # Return max of the three
    if left_max >= right_max and left_max >= cross_max:
        return left_max
    elif right_max >= left_max and right_max >= cross_max:
        return right_max
    else:
        return cross_max


def max_crossing_subarray(diff, low, mid, high):
    current_sum = 0
    left_sum = diff[mid]

    # Calculate max sum in left starting at mid point and moving left
    for i in range(mid, low - 1, -1):
        current_sum += diff[i]
        if current_sum > left_sum:
            left_sum = current_sum

    # Calculate max sum in right starting at mid + 1 and moving right
    # Reset sum
    current_sum = 0
    # Handle possible out of bounds access for mid + 1
    if mid + 1 <= high:
        right_sum = diff[mid + 1]
    else:
        right_sum = 0  # Right has no elements

    for i in range(mid + 1, high + 1, 1):
        current_sum += diff[i]
        if current_sum > right_sum:
            right_sum = current_sum
    # Combine two sums
    cross_sum = right_sum + left_sum

    return cross_sum


def main():

    # Check command line args
    if len(sys.argv) != 2:
        print("Usage: python project1.py input.txt")
        return

    file_name = sys.argv[1]

    # Read in stock prices from file and create array of floats
    prices = read_stocks(filename=file_name)

    if len(prices) <= 1:
        print(f"One or less prices. The optimal solution for {file_name} is 0")
        return
    #
    optimal_profit = find_max_profit(prices)

    print(f"The optimal solution for {file_name} is {optimal_profit:.2f}.")


if __name__ == "__main__":
    main()
