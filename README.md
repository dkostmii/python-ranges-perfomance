# python-ranges-perfomance

This project runs tests for perfomance of finding if big number is in range in various cases.

Results of testing are showing that Python handles this easily:

```text
Tests are in form:
Test name -> 12:34:56.789 or 0.01 ns

Big number = 1000000000000000

Big number in range (original) -> 0.14 ns
Big number in range of every second -> 0.01 ns
Big number in range of every third -> 0.01 ns
Big number in range of every random -> 0.04 ns
Random number in range of every random -> 0.05 ns
Random number, bigger than big number, is in range of every random -> 0.02 ns
Random negative number in range of every random -> 0.04 ns
```
