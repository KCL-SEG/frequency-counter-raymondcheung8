"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        theItem = str(item)
        if theItem in frequencies:
            frequencies[theItem] += 1
        else:
            frequencies[theItem] = 1
    return frequencies
