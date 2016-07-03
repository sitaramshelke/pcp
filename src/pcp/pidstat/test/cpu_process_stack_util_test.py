import unittest
from mock import Mock
import  mock
from pcp_pidstat import CpuProcessStackUtil


class TestCpuProcessStackUtil(unittest.TestCase):

    def current_values_side_effect(self, metric):
        if metric == 'proc.psinfo.pid':
            return {1: 1, 2: 2, 5: 5, 10: 10}

    def test_get_processes(self):
        metric_repository = mock.Mock()
        cpu_process_stack_util = CpuProcessStackUtil(metric_repository)
        metric_repository.current_values = mock.Mock(side_effect=self.current_values_side_effect)

        processes_list = cpu_process_stack_util.get_processes()

        self.assertEquals(len(processes_list),4)

if __name__ == '__main__':
    unittest.main()
