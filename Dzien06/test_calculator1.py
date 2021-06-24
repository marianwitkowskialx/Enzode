
# Testy jednostkowe przy uzyciu unittest
from unittest import TestCase
from calculator import Calculator
from unittest.mock import patch

class TestCalculator(TestCase):

    def setUp(self):
        self._calc = Calculator()

    def tearDown(self) -> None:
        print("Koniec testów")
        self._calc = None

    def test_add(self):
        self.assertEqual( self._calc.add(10, 5), 15)
        self.assertEqual( self._calc.add(-1, 1), 0)
        self.assertEqual( self._calc.add(-1, -1), -2)

    def test_div(self):
        self.assertEqual( self._calc.div(10,2), 5 )
        self.assertAlmostEqual( self._calc.div(10,3), 3.33333333, delta=0.01 )

        with self.assertRaises(ValueError):
            self._calc.div(10, 0)

    @patch('os.listdir')
    def test_dir_in_list(self, listdir_mock):
        listdir_mock.return_value = ['tmp1', 'tmp2']
        assert self._calc.dir_exist('tmp1')