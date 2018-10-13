from django.test import TestCase
import unittest
import IcarusDP.validator as vd
from calendar import IllegalMonthError

class ValidatorTestCase(unittest.TestCase):

    valid_iata = ['DME', "ABA", "VRN"]
    invalid_iata = ['QQQ', 'qwedasd', 'DmE']
    valid_datetime = map(vd.dt_tuple_format,
                         [vd.dt_now,
                          vd.current_datetime(vd.dt_now.year + 1, vd.dt_now.month, vd.dt_now.day)])

    def test_iata_validation(self):
        for iata in self.valid_iata:
            self.assertTrue(vd.is_iatacode_valid(iata))
        for iata in self.invalid_iata:
            self.assertFalse(vd.is_iatacode_valid(iata))

    def test_datetime_validation(self):
        for datetime in self.valid_datetime:
            self.assertTrue(vd.is_datetime_valid(datetime))

        false_item = vd.dt_tuple_format(
                           vd.current_datetime(vd.dt_now.year + 4, vd.dt_now.month, vd.dt_now.day)
        )

        self.assertFalse(vd.is_datetime_valid(false_item))

        # Use calendar exception

        assert_item = vd.dt_tuple_format(
            vd.current_datetime(vd.dt_now.year, vd.dt_now.month + 10, vd.dt_now.day)
        )
        self.assertRaises(IllegalMonthError, vd.is_datetime_valid, assert_item)


if __name__ == '__main__':
    unittest.main()


