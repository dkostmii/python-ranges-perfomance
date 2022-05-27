# python-ranges-perfomance

This project runs tests for perfomance of finding if big number is in range in various cases.

## How to use

Type in your terminal:

```text
python main.py
```

To show results in nanoseconds:

```text
python main.py -ns
```

----

## Overview

Python version used:

```text
Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
```

Results of testing are showing that Python handles this easily:

```text
Range perfomance test
Test perfomance of finding if big number is in range in various cases

Tests are in form:
Test name -> 12.34 ns

Big number = 1000000000000000
Range = [0, 1000000000000001]

Big number in range (original) -> 0.02 ns
Big number in range of every second -> 0.01 ns
Big number in range of every third -> 0.01 ns
Big number in range of every random -> 0.08 ns
Random number in range of every random -> 0.02 ns
Random number, bigger than big number, is in range of every random -> 0.03 ns
Random negative number in range of every random -> 0.02 ns
```
