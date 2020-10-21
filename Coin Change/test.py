from solution import coinChange
import unittest

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_TARGET = "target"
KEY_COINS = "coins"


class SplitTestCase(unittest.TestCase):
    def setUp(self):
        self.tests = [
            {
                KEY_INPUT: {KEY_TARGET: 5, KEY_COINS: [1, 2, 3, 8]},
                KEY_EXPECTED: 5
            },
            {
                KEY_INPUT: {KEY_TARGET: 10, KEY_COINS: [10]},
                KEY_EXPECTED: 1
            },
            {
                KEY_INPUT: {KEY_TARGET: 10, KEY_COINS: [11]},
                KEY_EXPECTED: 0
            },
        ]

    def test_split_success(self):
        for test in self.tests:
            target = test[KEY_INPUT][KEY_TARGET]
            coins = test[KEY_INPUT][KEY_COINS]
            expected = test[KEY_EXPECTED]
            actual = coinChange(target, coins)
            print(f"coins = {coins}")
            print(f"target = {target}")
            print(f"expected = {expected} actual value: {actual}")
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
