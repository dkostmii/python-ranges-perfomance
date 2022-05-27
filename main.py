from util import msToNs, pluck
from timeit import timeit
from defs import testcases, bigNumber


def main():
  print("Tests are in form:")
  print("Test name -> 12:34:56.789 or 0.01 ns")
  print()

  print(f"Big number = {bigNumber}")
  print()

  for tc in testcases:
    (name, case) = pluck(tc, "name", "case")
    print(f"{name} -> " + msToNs(timeit(case, number=1)))


if __name__ == "__main__":
  main()
