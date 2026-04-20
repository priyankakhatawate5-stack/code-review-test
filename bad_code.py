import os
import json
import requests  # unused import

# Hardcoded secret - should be detected!
api_key = "sk-1234567890abcdef"
password = "supersecret123"

def process_data(x, y, z, a, b, c, d, e, f):
    if x > 0:
        if y > 0:
            if z > 0:
                if a > 0:
                    if b > 0:
                        return x + y + z + a + b
    return 0

def very_long_function():
    line1 = 1
    line2 = 2
    line3 = 3
    line4 = 4
    line5 = 5
    line6 = 6
    line7 = 7
    line8 = 8
    line9 = 9
    line10 = 10
    return line1 + line2 + line3
# test

def unused_function():
    print("This function is never called")
    continue
