#!/usr/bin/env python3

import copy
import random
import unittest

from src.merge import merge


class TestMerge(unittest.TestCase):

    def test_non_mutating(self):
        L1_orig = [1, 5, 9, 12]
        L2_orig = [2, 6, 10]
        L1 = copy.copy(L1_orig)
        L2 = copy.copy(L2_orig)
        merge(L1, L2)
        self.assertEqual(
            L1, L1_orig,
            msg="merge(%s, %s) must not modify its first input list! "
                "After the call L1 was %s but should still be %s."
                % (L1_orig, L2_orig, L1, L1_orig))
        self.assertEqual(
            L2, L2_orig,
            msg="merge(%s, %s) must not modify its second input list! "
                "After the call L2 was %s but should still be %s."
                % (L1_orig, L2_orig, L2, L2_orig))

    def test_first(self):
        L1 = [1, 5, 9, 12]
        L2 = [2, 6, 10]
        result = merge(L1, L2)
        self.assertIsInstance(
            result, list,
            msg=f"merge should return a list. Got {type(result)}.")
        self.assertEqual(
            result, sorted(L1 + L2),
            msg="Incorrect result for input lists %s and %s! merge assumes "
                "both inputs are already sorted and should interleave them "
                "into one sorted list." % (L1, L2))

    def test_random(self):
        L = sorted(random.randint(-100, 100) for _ in range(30))
        # Choose randomly 20 elements out of 30 to be in list L1, rest in L2
        indices = set(random.sample(range(30), 20))
        L1 = []
        L2 = []
        for i, x in enumerate(L):
            if i in indices:
                L1.append(x)
            else:
                L2.append(x)
        result = merge(L1, L2)
        self.assertEqual(
            len(result), len(L),
            msg="Incorrect length of result list for input lists %s and %s!"
                % (L1, L2))
        self.assertEqual(
            result, L,
            msg="Incorrect result for input lists %s and %s!" % (L1, L2))


if __name__ == '__main__':
    unittest.main()
