# Handy tool for receiving data via redirection in console
from collections import deque

def read_input(input):
    lines = deque(input)
    number_of_test_cases = lines.popleft()
    return (number_of_test_cases, lines)

if __name__ == '__main__':
    import sys
    read_input(sys.stdin)
