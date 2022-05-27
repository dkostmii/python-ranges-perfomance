from math import floor
from typing import Union, Any
from sys import argv


def indexExists(l: list[Any], id: int) -> bool:
  return 0 <= id < len(l)


# Catch argument (pass "ns" for -ns) from command-line execution
#
# Catches both switch (just -ns)
# which returns True
#
# and values (-ns somesillystuff)
# which returns "somesillystuff"
#
# if argument is not provided
# returns False
def catchArg(arg: str) -> Any:
  if len(argv) < 2:
    return False
  
  try:
    arg = "-" + arg
    normArgv = list(map(lambda arg: arg.lower(), argv))
    argId = normArgv.index(arg)
    if indexExists(normArgv, argId + 1):
      return normArgv[argId + 1]
    else:
      return True
  except:
    return False

# Formats time as 
# for hh, mm, ss provided - 12:34:56
# for hh, mm, ss, ms provided - 12:34:56.789
# for ns provided - 12.34 ns (ignores hh, mm, ss)
def timeFmt(
    hh: Union[int, None] = None,
    mm: Union[int, None] = None,
    ss: Union[int, None] = None,
    ms: Union[int, None] = None,
    ns: Union[float, None] = None
  ) -> str:
  if ns is None:
    if hh is None or mm is None or ss is None:
      raise TypeError("One of the args: hh, mm or ss is None")

    if ms is None:
      return "{:02d}:{:02d}:{:02d}".format(hh, mm, ss)
    else:
      return "{:02d}:{:02d}:{:02d}.{:03d}".format(hh, mm, ss, ms)
  else:
    return "{:02.2f} ns".format(round(ns, 2))


# Used to map dict item to tuple of specified args
# Example:
#
# d = { "a": 1, "b": 2 }
# (a, b) = pluck(d, "a", "b")
def pluck(dict: dict[str, Any], *args: str):
  return (dict[arg] for arg in args)


# Functions below are calculating time components
# And returning apropriate time string
def secondsToTime(seconds: Union[int, float] = 0) -> str:
  seconds = abs(seconds)

  ss = int(seconds % 60)
  mm = int(floor(seconds / 60) % 60)
  hh = int(floor(((seconds / 60) / 60)))

  return timeFmt(hh, mm, ss)


def msToTime(milliseconds: Union[int, float] = 0) -> str:
  milliseconds = abs(milliseconds)

  ms = int(milliseconds % 1000)
  ss = int(floor(milliseconds / 1000) % 60)
  mm = int(floor(milliseconds / 1000 / 60) % 60)
  hh = int(floor(milliseconds / 1000 / 60 / 60) % 60)

  return timeFmt(hh, mm, ss, ms)


def msToNs(milliseconds: Union[int, float] = 0) -> str:
  nanoseconds = milliseconds * 1000
  return timeFmt(ns=nanoseconds)
