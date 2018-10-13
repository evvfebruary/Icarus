import unittest
import IcarusDP.validator as vd
from datetime import datetime as dt
import requests as rq
from IcarusDP import mocked_requests as mocked


class ValidatorTestCase(unittest.TestCase):

    valid_iata = ['DME', "ABA", "VRN"]
    invalid_iata = ['QQQ', 'qwedasd', 'DmE']

    def test_iata_validation(self):
        for iata in self.valid_iata:
            self.assertTrue(vd.is_iatacode_valid(iata))
        for iata in self.invalid_iata:
            self.assertFalse(vd.is_iatacode_valid(iata))

    def test_datetime_validation(self):
        self.assertTrue(vd.is_datetime_valid(dt(vd.dt_now.year + 1,
                                                vd.dt_now.month,
                                                vd.dt_now.day)))
        self.assertRaises(ValueError, dt, 2018, 11, 100)
        self.assertRaises(ValueError, dt, 2044, 234234, 100)
        self.assertFalse(vd.is_datetime_valid(dt(2018, 3, 3)))
        self.assertFalse(vd.is_datetime_valid(dt(2044, 3, 3)))


class APITestCase(unittest.TestCase):
    root_url = "http://127.0.0.1:8000/"
    token = '850652a6a769687a7f10af2768e458a4c7464dfd'

    def request_wt(self, json):
        return rq.post(self.root_url + "dpcheck/", json=json, headers={'Authorization': 'Token ' + self.token}).json()

    def test_get_token_case(self):
        request = rq.post(self.root_url + 'get-api-token/',
                          json={"username": "usertoken", "password": "s7testcasetoken"})
        self.assertEqual(list(request.json().keys()), ['token'])

    def test_token_required_case(self):
        request = rq.post(self.root_url + 'dpcheck/')
        self.assertEqual(request.json()['detail'], 'Authentication credentials were not provided.')

    def test_iata_case(self):
        response = self.request_wt(mocked.invalid_iata)
        self.assertEqual(response['Handled error']['origin'], ['Wrong IATA code'])

    def test_adt_case(self):
        response = self.request_wt(mocked.invalid_adt_count)
        self.assertEqual(response['Handled error']['ptcs'], ['Wrong adult passengers fields'])

    def test_json_case(self):
        response = self.request_wt(mocked.invalid_json_frm)
        self.assertEqual(response['Handled error']['ptcs'], ['This field is required.'])

    def test_departure(self):
        response = self.request_wt(mocked.invalid_departure)
        self.assertEqual(response['Handled error']['departure'],
         ['Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]].'])

    # Remove when campaign generator will available
    def test_valid(self):
        response = self.request_wt(mocked.valid_json)
        self.assertEqual(response['received data'],
                         mocked.valid_json)


if __name__ == '__main__':
    unittest.main()


