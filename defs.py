from math import floor
from random import randint

bigNumber = 1000000000000000


def original() -> bool:
  return bigNumber in range(bigNumber + 1)


def everySecond() -> bool:
  return bigNumber in range(0, bigNumber + 1, 2)


def everyThird() -> bool:
  return bigNumber in range(0, bigNumber + 1, 3)


def everyHalf() -> bool:
  return bigNumber in range(0, bigNumber + 1, int(floor(bigNumber / 2)))


def everyRandom() -> bool:
  return bigNumber in range(0, bigNumber + 1, randint(1, bigNumber))


def randomEveryRandom() -> bool:
  return randint(0, bigNumber) in range(0, bigNumber + 1, randint(1, bigNumber))


def randomEveryRandomOutsideOfRangePos() -> bool:
  return randint(bigNumber + 1, 2 * bigNumber) in range(0, bigNumber + 1, randint(1, bigNumber))


def randomEveryRandomOutsideOfRangeNeg() -> bool:
  return randint(-2 * bigNumber, -1) in range(0, bigNumber + 1, randint(1, bigNumber))

testDescription = {
  "name": "Range perfomance test",
  "description": "Test perfomance of finding if big number is in range in various cases",
  "definitions": f"Big number = {bigNumber}\nRange = [0, {bigNumber + 1}]"
}


testcases = [{
  "name": "Big number in range (original)",
  "case": original
}, {
  "name": "Big number in range of every second",
  "case": everySecond
}, {
  "name": "Big number in range of every third",
  "case": everyThird
}, {
  "name": "Big number in range of every random",
  "case": everyRandom
}, {
  "name": "Random number in range of every random",
  "case": randomEveryRandom
}, {
  "name": "Random number, bigger than big number, is in range of every random",
  "case": randomEveryRandomOutsideOfRangePos
}, {
  "name": "Random negative number in range of every random",
  "case": randomEveryRandomOutsideOfRangeNeg
}]
