#!/usr/bin/env pmpython
import sys
import unittest
if sys.version_info[0] < 3:
    from mock import Mock
else:
    from unittest.mock import Mock
from pcp_mpstat import SoftInterruptUsage

class TestSoftInterruptUsage(unittest.TestCase):
    def setUp(self):
        self.metric_repository = Mock()
        self.metric_repository.current_values = Mock(side_effect = self.current_value_side_effect)
        self.interrupt_metric = ['kernel.percpu.softirqs.RCU','kernel.percpu.softirqs.HRTIMER','kernel.percpu.softirqs.SCHED']

    def current_value_side_effect(self, metric):
        if metric == 'hinv.map.cpu_num':
            return {'0':0,'1':1,'2':2,'3':3}
        return None

    def test_get_percpu_interrupts(self):
        soft_interrupt_usage = SoftInterruptUsage(1.34, self.metric_repository, self.interrupt_metric)

        percpu_interrupts = soft_interrupt_usage.get_percpu_interrupts()

        self.assertEqual(len(percpu_interrupts), 4)

if __name__ == "__main__":
    unittest.main()
