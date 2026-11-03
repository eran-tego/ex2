#!/usr/bin/env python3
"""Check whether a number is prime."""

from __future__ import annotations

import argparse
import math
import sys


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.isqrt(n)) + 1
    for candidate in range(3, limit, 2):
        if n % candidate == 0:
            return False
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check whether a number is prime.")
    parser.add_argument("number", type=int, help="Integer to test for primality")
    args = parser.parse_args(argv)

    if is_prime(args.number):
        print(f"{args.number} is prime")
        return 0

    print(f"{args.number} is not prime")
    return 1


if __name__ == "__main__":
    sys.exit(main())
