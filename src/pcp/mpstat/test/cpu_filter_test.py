#!/usr/bin/env pmpython
import unittest
from mock import Mock
from pcp_mpstat import CpuFilter

class TestCpuFilter(unittest.TestCase):
    def setUp(self):
        self.mpstat_options = Mock()
        self.mpstat_options.cpu_list = None
        self.cpus = [Mock(
                        cpu_number = Mock(return_value = 0),
                        cpu_online = Mock(return_value = 1)),
                    Mock(
                            cpu_number = Mock(return_value = 1),
                            cpu_online = Mock(return_value = 1)),
                    Mock(
                            cpu_number = Mock(return_value = 2),
                            cpu_online = Mock(return_value = 0)),
                    ]

    def test_filter_cpus_all(self):
        self.mpstat_options.cpu_list = "ALL"
        cpu_filter = CpuFilter(self.mpstat_options)

        cpu_list = cpu_filter.filter_cpus(self.cpus)

        self.assertEqual(len(cpu_list), 3)

    def test_filter_cpus_on(self):
        self.mpstat_options.cpu_list = "ON"
        cpu_filter = CpuFilter(self.mpstat_options)

        cpu_list = cpu_filter.filter_cpus(self.cpus)

        self.assertEqual(len(cpu_list), 2)

    def test_filter_cpus_list(self):
        self.mpstat_options.cpu_list = [1]
        cpu_filter = CpuFilter(self.mpstat_options)

        cpu_list = cpu_filter.filter_cpus(self.cpus)

        self.assertEqual(len(cpu_list), 1)

if __name__ == '__main__':
    unittest.main()
