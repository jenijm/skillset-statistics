#!/usr/bin/env python3
"""Calculate the mean, median, and mode of a small set of numbers."""

import argparse
import statistics
import sys
from typing import Dict, List, Union


Number = Union[int, float]


def calculate_statistics(numbers: List[Number]) -> Dict[str, object]:
    """Return the mean, median, and mode or modes for a non-empty list."""
    if not numbers:
        raise ValueError("At least one number is required.")

    return {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "modes": statistics.multimode(numbers),
    }


def format_number(number: Number) -> str:
    """Display whole-valued results without an unnecessary decimal part."""
    return f"{number:g}"


def parse_numbers(values: List[str]) -> List[float]:
    """Convert command-line or interactive values to numbers."""
    try:
        return [float(value) for value in values]
    except ValueError as error:
        raise ValueError("Every value must be a valid number.") from error


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate mean, median, and mode from a set of numbers."
    )
    parser.add_argument(
        "numbers",
        nargs="*",
        help="Numbers separated by spaces; prompts interactively when omitted.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        raw_values = args.numbers
        if not raw_values:
            entered = input("Enter numbers separated by spaces: ").strip()
            raw_values = entered.split()

        numbers = parse_numbers(raw_values)
        results = calculate_statistics(numbers)
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.", file=sys.stderr)
        return 1
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    modes = results["modes"]
    mode_text = ", ".join(format_number(mode) for mode in modes)

    print(f"Numbers: {', '.join(format_number(number) for number in numbers)}")
    print(f"Mean: {format_number(results['mean'])}")
    print(f"Median: {format_number(results['median'])}")
    print(f"Mode: {mode_text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
