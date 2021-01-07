import unittest
from logic.abilities import (
    IllegalAbilityError,
    TargetCountMismatchError,
    NoTargetsError,
    AbilityData,
)


class TestAbilityData(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == "__main__":
    unittest.main()
