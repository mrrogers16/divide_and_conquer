


def read_stocks(filename):
    
    prices = [] 

    # Read in specified file and return array of floats
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Strip any leading/trailing whitespace chars
                line = line.strip()
                # Skip empty lines
                if line == '':
                    continue
                # Convert line to float and append to price list
                try:
                    price = float(line)
                    prices.append(price)
                except ValueError:
                    print(f"Error: The line '{line}' is not a valid number.")
                    exit(1)
        
        # Return array of floats             
        return prices
    
    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")

if __name__ == '__main__':