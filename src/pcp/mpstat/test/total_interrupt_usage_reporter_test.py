#!/usr/bin/env pmpython
import unittest
from mock import Mock
from mock import call
from pcp_mpstat import TotalInterruptUsageReporter

class TestTotalInterruptUsageReporter(unittest.TestCase):

    def test_print_report_without_cpu_filter(self):
        timestamp = "2016-19-07 IST"
        total_interrupt_usage = Mock()
        total_interrupt_usage.total_interrupt_per_delta_time = Mock(return_value = 1.23)
        options = Mock()
        options.cpu_list = None
        options.cpu_filter = False
        printer = Mock()
        cpu_filter = Mock()
        report = TotalInterruptUsageReporter(cpu_filter, printer, options)

        report.print_report(total_interrupt_usage, timestamp)

        printer.assert_called_with('2016-19-07 IST\tall  \t1.23 ')

    def test_print_report_with_filtered_cpus(self):
        timestamp = "2016-19-07 IST"
        total_interrupt_usage = Mock()
        total_interrupt_usage.total_interrupt_per_delta_time = Mock(return_value = 1.23)
        options = Mock()
        options.cpu_list = 'ALL'
        options.cpu_filter = True
        printer = Mock()
        cpu_filter = Mock()
        cpu_interrupt = Mock()
        cpu_interrupt.cpu_number = Mock(return_value=0)
        cpu_interrupt.value = Mock(return_value=2.4)
        cpu_filter.filter_cpus = Mock(return_value=[cpu_interrupt])
        report = TotalInterruptUsageReporter(cpu_filter, printer, options)

        report.print_report(total_interrupt_usage, timestamp)

        calls = [call('\nTimestamp\tCPU  \tintr/s'),
                call('2016-19-07 IST\tall  \t1.23 '),
                call('2016-19-07 IST\t0    \t2.4  ')]

        printer.assert_has_calls(calls)

if __name__ == "__main__":
    unittest.main()
