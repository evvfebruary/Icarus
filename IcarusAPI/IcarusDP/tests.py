import unittest
import IcarusDP.validator as vd
from datetime import datetime as dt


class ValidatorTestCase(unittest.TestCase):

    valid_iata = ['DME', "ABA", "VRN"]
    invalid_iata = ['QQQ', 'qwedasd', 'DmE']

    def test_iata_validation(self):
        for iata in self.valid_iata:
            self.assertTrue(vd.is_iatacode_valid(iata))
        for iata in self.invalid_iata:
            self.assertFalse(vd.is_iatacode_valid(iata))

    def test_datetime_validation(self):
        self.assertRaises(ValueError, dt, 2018, 11, 100)
        self.assertRaises(ValueError, dt, 2044, 234234, 100)
        self.assertFalse(vd.is_datetime_valid(dt(2018, 3, 3)))
        self.assertFalse(vd.is_datetime_valid(dt(2044, 3, 3)))


if __name__ == '__main__':
    unittest.main()


