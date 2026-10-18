# Mean, Median, and Mode Calculator

A Python command-line program that calculates the mean, median, and mode from a small set of numbers.

## Definitions

- **Mean:** the sum of all numbers divided by the number of values.
- **Median:** the middle value after sorting the numbers.
- **Mode:** the value that appears most often. Multiple modes are displayed when tied.

## Requirements

- Python 3.8 or newer

No external dependencies are required.

## Run with numbers

```bash
python3 statistics_calculator.py 2 4 4 6 8
```

Output:

```text
Numbers: 2, 4, 4, 6, 8
Mean: 4.8
Median: 4
Mode: 4
```

## Run interactively

```bash
python3 statistics_calculator.py
```

Enter the numbers separated by spaces when prompted.

## Run the tests

```bash
python3 -m unittest -v
```

The tests cover single and multiple modes, odd and even data sets, decimal and negative values, empty input, and invalid input.
