import unittest
from blockchain.statistics import *


class TestGetChart(unittest.TestCase):
    def test_getChart(self):
        chart_data = get_chart('total-bitcoins', '5weeks', '8hours')
        self.assertEqual('ok', chart_data.status)
        self.assertEqual('Bitcoins in circulation', chart_data.name)
        self.assertEqual('BTC', chart_data.unit)
        self.assertEqual('day', chart_data.period)
        self.assertEqual('The total number of bitcoins that have already been mined; in other words, the current supply of bitcoins on the network.', chart_data.description)


class TestGetPools(unittest.TestCase):
    def test_getPools(self):
        pools = get_pools('5days')
        self.assertTrue(len(pools) > 0)


if __name__ == '__main__':
    unittest.main()