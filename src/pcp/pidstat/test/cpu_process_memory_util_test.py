import unittest
from mock import Mock
import  mock
from pcp_pidstat import CpuProcessMemoryUtil


class TestCpuProcessMemoryUtil(unittest.TestCase):

    def current_values_side_effect(self, metric):
        if metric == 'proc.psinfo.pid':
            return {1: 1, 2: 2, 5: 5, 10: 10}

    def test_get_processes(self):
        metric_repository = mock.Mock()
        cpu_process_memory_util = CpuProcessMemoryUtil(metric_repository)
        metric_repository.current_values = mock.Mock(side_effect=self.current_values_side_effect)

        processes_list = cpu_process_memory_util.get_processes(1.34)

        self.assertEquals(len(processes_list),4)

if __name__ == '__main__':
    unittest.main()
