import unittest

import definition

# this is a stub, it'll fail

class DefinitionTest(unittest.TestCase):
    def test_one_known_word(self):
        self.assertEqual('house: ˈhau̇s : a building that serves as living quarters for one or a few families', definition.def_lookup("house"))


if __name__ == '__main__':
    unittest.main()
