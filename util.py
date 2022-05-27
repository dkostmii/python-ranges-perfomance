from math import floor
from typing import Union, Any


def pluck(dict: dict[str, Any], *args: str):
  return (dict[arg] for arg in args)


def secondsToTime(seconds: Union[int, float] = 0) -> str:
  seconds = abs(seconds)

  ss = int(seconds % 60)
  mm = int(floor(seconds / 60) % 60)
  hh = int(floor(((seconds / 60) / 60)))

  return "{:02d}:{:02d}:{:02d}".format(hh, mm, ss)


def msToTime(milliseconds: Union[int, float] = 0) -> str:
  milliseconds = abs(milliseconds)

  ms = int(milliseconds % 1000)
  ss = int(floor(milliseconds / 1000) % 60)
  mm = int(floor(milliseconds / 1000 / 60) % 60)
  hh = int(floor(milliseconds / 1000 / 60 / 60) % 60)

  return "{:02d}:{:02d}:{:02d}.{:03d}".format(hh, mm, ss, ms)


def msToNs(milliseconds: Union[int, float] = 0) -> str:
  nanoseconds = round(milliseconds * 1000, 2)

  return "{:02.2f} ns".format(nanoseconds)