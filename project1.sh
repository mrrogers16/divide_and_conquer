
#!/bin/bash

# Check command line args
if [ "$#" -ne 1 ]; then
    echo "Usage: project1.sh input.txt"
    exit 1
fi

# Check for input file
input_file="$1"
if [ ! -f "$input_file" ]; then
    echo "Error: File '$input_file' not found!"
    exit 1
fi

# Run python script 
python3 project1.py "$input_file"