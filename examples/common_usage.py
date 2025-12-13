#!/usr/bin/env python3
"""
A small runnable Python program demonstrating common language features:
- input / output
- functions
- flow control (for, if/else)
- data structures: numbers, list (array), dict (map), set
- basic file I/O

Run: `python3 examples/common_usage.py` (will prompt for input)
You can pipe sample input for automated runs.
"""
from typing import List, Dict, Tuple
import statistics


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to the demo."


def compute_stats(numbers: List[float]) -> Dict[str, float]:
    # Demonstrates numbers, for-loop, if/else
    if not numbers:
        return {"count": 0, "sum": 0.0, "mean": 0.0, "min": 0.0, "max": 0.0}

    total = 0.0
    count = 0
    _min = numbers[0]
    _max = numbers[0]

    for n in numbers:
        total += n
        count += 1
        if n < _min:
            _min = n
        if n > _max:
            _max = n

    mean = total / count if count else 0.0
    return {"count": count, "sum": total, "mean": mean, "min": _min, "max": _max}


def counts_map(numbers: List[float]) -> Dict[float, int]:
    # Demonstrates map/dict usage and iteration
    counts: Dict[float, int] = {}
    for n in numbers:
        counts[n] = counts.get(n, 0) + 1
    return counts


def demonstrate_collections(numbers: List[float]) -> None:
    # List (array)
    print("\nList operations:")
    numbers_copy = numbers.copy()
    print(" Original:", numbers_copy)
    numbers_copy.append(42)
    print(" After append:", numbers_copy)
    print(" Slice [1:4]:", numbers_copy[1:4])

    # Set
    print("\nSet operations:")
    s = set(numbers)
    print(" Unique values (set):", s)
    other = {2, 42, 100}
    print(" Union:", s | other)
    print(" Intersection:", s & other)

    # Dict (map)
    print("\nDict (counts):")
    cnts = counts_map(numbers)
    for value, c in cnts.items():
        print(f"  {value} appears {c} time(s)")


def write_results_to_file(path: str, summary: Dict[str, float], counts: Dict[float, int]) -> None:
    # Basic file I/O
    with open(path, "w", encoding="utf-8") as f:
        f.write("Summary of numbers\n")
        for k, v in summary.items():
            f.write(f"{k}: {v}\n")
        f.write("\nCounts:\n")
        for val, c in counts.items():
            f.write(f"{val}: {c}\n")


def parse_numbers(input_str: str) -> List[float]:
    # Parse comma-separated numbers with error handling
    nums: List[float] = []
    for token in input_str.split(","):
        token = token.strip()
        if not token:
            continue
        try:
            if "." in token:
                n = float(token)
            else:
                n = int(token)
        except ValueError:
            print(f" Skipping invalid token: {token}")
            continue
        nums.append(float(n))
    return nums


def main() -> None:
    print("=== Python Common Usage Demo ===")

    # Input / Output: get name
    name = input("Enter your name (or press Enter to use 'Guest'): ").strip()
    if not name:
        name = "Guest"
    print(greet(name))

    # Show number types and arithmetic
    print("\nNumber examples:")
    a = 7  # int
    b = 3.5  # float
    print(f" a = {a} (type {type(a).__name__}), b = {b} (type {type(b).__name__})")
    print(" a + b =", a + b)
    print(" a / 2 =", a / 2)

    # Ask for numbers or use sample
    nums_input = input("Enter numbers separated by commas (e.g. 1,2,3.5) or press Enter to use sample: ").strip()
    if nums_input:
        numbers = parse_numbers(nums_input)
        if not numbers:
            print(" No valid numbers entered — using default sample list.")
            numbers = [3, 7, 2, 9.5, 3]
    else:
        numbers = [3, 7, 2, 9.5, 3]

    print("\nNumbers to analyze:", numbers)

    # Compute statistics (flow control demonstrated inside function)
    summary = compute_stats(numbers)
    print("\nSummary:")
    for k, v in summary.items():
        print(f" {k}: {v}")

    # Counts (map/dict) and collections demo
    cnts = counts_map(numbers)
    demonstrate_collections(numbers)

    # Demonstrate built-in utilities
    try:
        median = statistics.median(numbers)
        print("\nMedian (from statistics module):", median)
    except statistics.StatisticsError:
        print(" Could not compute median for empty list")

    # Write results to file
    out_path = "results.txt"
    write_results_to_file(out_path, summary, cnts)
    print(f"\nResults written to {out_path}")

    print("\nDemo complete. Goodbye!")


if __name__ == "__main__":
    main()
