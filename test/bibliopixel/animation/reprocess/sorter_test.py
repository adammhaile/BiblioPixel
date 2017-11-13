import unittest
from bibliopixel.animation.reprocess import functions
from bibliopixel.util.colors.conversions import hsv2rgb_raw

# Map letters to colors so that we can read inputs and outputs.
COLORS = {ch: hsv2rgb_raw((ord(ch), 127, 127)) for ch in 'abcdef'}
INVERSE_COLORS = {c: ch for (ch, c) in COLORS.items()}


def sorter(input):
    s = [COLORS[i] for i in input]
    functions.sorter(s)
    return ''.join(INVERSE_COLORS[c] for c in s)


class SorterTest(unittest.TestCase):
    def test_empty(self):
        self.assertEquals(sorter(''), '')

    def test_one(self):
        self.assertEquals(sorter('a'), 'a')

    def test_one(self):
        self.assertEquals(sorter('ba'), 'ab')

    def test_sorted(self):
        self.assertEquals(sorter('a'), 'a')
        self.assertEquals(sorter('ab'), 'ab')
        self.assertEquals(sorter('abc'), 'abc')
        self.assertEquals(sorter('abcd'), 'abcd')
        self.assertEquals(sorter('abcde'), 'abcde')

    def test_reverse(self):
        results = ['fedcba']

        while True:
            prev = results[-1]
            next = sorter(prev)
            if next == prev:
                break
            results.append(next)

        expected = [
            'fedcba',
            'efdcba',
            'edfcba',
            'defcba',
            'decfba',
            'dcefba',
            'cdefba',
            'cdebfa',
            'cdbefa',
            'cbdefa',
            'bcdefa',
            'bcdeaf',
            'bcdaef',
            'bcadef',
            'bacdef',
            'abcdef',
        ]

        self.assertEquals(results, expected)
