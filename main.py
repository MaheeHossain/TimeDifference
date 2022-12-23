# Code written by Mahee Hossain: https://github.com/MaheeHossain
# Takes input from an input.txt file

import sys

from readFiles import readInput

INPUT_FILE = './Test_cases/Input.txt'
DEMO_FILE = './Test_cases/Demo.txt'

OUTPUT_FILE = "output.txt"

if __name__ == '__main__':
    original_stdout = sys.stdout
    fptr = open(OUTPUT_FILE, 'w')
    sys.stdout = fptr

    # Get the times
    times = readInput(DEMO_FILE)

    for time in times:
      print(time)