import unittest
from mock import Mock
from pcp_mpstat import HardInterruptUsage

class TestHardInterruptUsage(unittest.TestCase):
    def setUp(self):
        self.metric_repository = Mock()
        self.metric_repository.current_values = Mock(side_effect = self.current_value_side_effect)
        self.interrupt_metric = ['kernel.percpu.interrupts.PIW','kernel.percpu.interrupts.PIN','kernel.percpu.interrupts.MIS']

    def current_value_side_effect(self, metric):
        if metric == 'hinv.map.cpu_num':
            return {'0':0,'1':1,'2':2,'3':3}
        return None

    def test_get_percpu_interrupts(self):
        hard_interrupt_usage = HardInterruptUsage(1.34, self.metric_repository, self.interrupt_metric)

        percpu_interrupts = hard_interrupt_usage.get_percpu_interrupts()

        self.assertEqual(len(percpu_interrupts), 4)

if __name__ == "__main__":
    unittest.main()
