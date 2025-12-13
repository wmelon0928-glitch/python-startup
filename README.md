# python-startup

A tiny repository with a runnable Python demo that illustrates common language features
such as input/output, functions, flow control, and basic data structures (numbers, list,
dictionary, set).

Files:

- `examples/common_usage.py` — A self-contained demo script. It prompts for a name and a
	comma-separated list of numbers, computes simple statistics, demonstrates lists,
	dictionaries and sets, and writes `results.txt`.

Usage:

Run interactively:

```bash
python3 examples/common_usage.py
```

Run with piped input (example):

```bash
printf "Alice\n1,2,3,3.5,2\n" | python3 examples/common_usage.py
```

The script will write `results.txt` to the repository root with a short summary.

This repository is intended as a gentle example for people learning Python.
