#!/usr/bin/env python3
"""
A small runnable Python program demonstrating common language features:
You can pipe sample input for automated runs.
"""
from typing import List, Dict, Tuple


def xxx() -> None:
    print("=== Python Common Usage Demo ===")

    # Input / Output: get name
    name = input("Enter your name (or press Enter to use 'Guest'): ").strip()
    if not name:
        name = "Guest"
    
    print(f"Hello! My name is {name}, type=type({type(name)})")
    print(f"\nDemo complete. Goodbye! {__name__}")


xxx()

# Run the main function
# if __name__ == "__main__":
#     main()
