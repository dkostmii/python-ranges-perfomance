from util import msToNs, msToTime, timeFmt, pluck, catchArg
from timeit import timeit
from defs import testcases, testDescription

ns = catchArg("-ns")
fmt = timeFmt(ns = 12.34) if ns else timeFmt(12, 34, 56, 789)

def main():
  (name, description, definitions) = pluck(testDescription, "name", "description", "definitions")
  print(name)
  print(description)
  print()

  print("Tests are in form:")
  print(f"Test name -> {fmt}")
  print()

  print(definitions)
  print()

  for tc in testcases:
    (name, case) = pluck(tc, "name", "case")

    result = timeit(case, number=1)
    formatted = msToNs(result) if ns else msToTime(result)

    print(f"{name} -> " + formatted)


if __name__ == "__main__":
  main()
