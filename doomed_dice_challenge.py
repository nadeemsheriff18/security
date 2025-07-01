from itertools import product
from collections import Counter

def get_distribution(die1, die2):
    distribution = Counter()
    for a in die1:
        for b in die2:
            distribution[a + b] += 1
    return distribution

def get_standard_distribution():
    return get_distribution(range(1, 7), range(1, 7))

def doomed_dice():
    standard = get_standard_distribution()

    # All combinations of 6 values from {1,2,3,4} for die A
    for die_a in product(range(1, 5), repeat=6):
        # Try values for die B from 1 to 18
        for die_b in product(range(1, 19), repeat=6):
            if get_distribution(die_a, die_b) == standard:
                return die_a, die_b  # Found a match

die_a, die_b = doomed_dice()

print("Die A:", die_a)
print("Die B:", die_b)
