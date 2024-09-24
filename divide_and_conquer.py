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


def main():
    # Take in file name
    # TODO Set up command line arguments to take in file name from user
    file_name = "small_input.txt"

    # Read in stock prices from file and create array of floats
    prices = read_stocks(filename=file_name)

    if len(prices) <= 1:
        print(f"The optimal solution for {file_name} is 0")
        return
    #
    optimal_profit = find_max_profit(prices)


if __name__ == "__main__":
    main()
