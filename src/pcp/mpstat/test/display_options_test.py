#!/usr/bin/env pmpython
import unittest
from mock import Mock
from pcp_mpstat import DisplayOptions

class TestDisplayOptions(unittest.TestCase):
    def setUp(self):
        self.mpstat_options = Mock()
        self.mpstat_options.cpu_list = None
        self.mpstat_options.cpu_filter = False
        self.mpstat_options.options_all = False
        self.mpstat_options.interrupts_filter = False
        self.mpstat_options.interrupt_type = None
        self.mpstat_options.no_options = True

    def test_display_cpu_usage_summary(self):
        display_options = DisplayOptions(self.mpstat_options)

        self.assertTrue(display_options.display_cpu_usage_summary())

    def test_display_total_cpu_usage_with_type_sum(self):
        self.mpstat_options.interrupts_filter = True
        self.mpstat_options.interrupt_type = "SUM"

        display_options = DisplayOptions(self.mpstat_options)

        self.assertTrue(display_options.display_total_cpu_usage())

    def test_display_total_cpu_usage_with_type_all(self):
        self.mpstat_options.interrupts_filter = True
        self.mpstat_options.interrupt_type = "ALL"

        display_options = DisplayOptions(self.mpstat_options)

        self.assertTrue(display_options.display_total_cpu_usage())

    def test_display_hard_interrupt_usage_with_type_cpu(self):
        self.mpstat_options.interrupts_filter = True
        self.mpstat_options.interrupt_type = "CPU"

        display_options = DisplayOptions(self.mpstat_options)

        self.assertTrue(display_options.display_hard_interrupt_usage())

    def test_display_hard_interrupt_usage_with_type_all(self):
        self.mpstat_options.interrupts_filter = True
        self.mpstat_options.interrupt_type = "ALL"

        display_options = DisplayOptions(self.mpstat_options)

        self.assertTrue(display_options.display_hard_interrupt_usage())

    def test_display_soft_interrupt_usage_with_type_scpu(self):
        self.mpstat_options.interrupts_filter = True
        self.mpstat_options.interrupt_type = "SCPU"

        display_options = DisplayOptions(self.mpstat_options)

        self.assertTrue(display_options.display_soft_interrupt_usage())

    def test_display_soft_interrupt_usage_with_type_all(self):
        self.mpstat_options.interrupts_filter = True
        self.mpstat_options.interrupt_type = "ALL"

        display_options = DisplayOptions(self.mpstat_options)

        self.assertTrue(display_options.display_soft_interrupt_usage())

if __name__ == '__main__':
    unittest.main()
