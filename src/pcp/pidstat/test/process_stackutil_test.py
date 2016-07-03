import mock
import unittest
from pcp_pidstat import ProcessStackUtil

class TestProcessStackUtil(unittest.TestCase):
    def setUp(self):
        self.__metric_repository = mock.Mock()
        self.__metric_repository.current_value = mock.Mock(side_effect=self.metric_repo_current_value_side_effect)

    def metric_repo_current_value_side_effect(self, metric_name,instance):
        if metric_name == 'proc.memory.vmstack' and instance == 1:
            return 136
        if metric_name == 'proc.psinfo.cmd' and instance == 1:
            return "test"
        if metric_name == 'proc.id.uid' and instance == 1:
            return 1
        if metric_name == 'proc.psinfo.pid' and instance == 1:
            return 1

    def test_stack_size(self):
        process_stack_usage = ProcessStackUtil(1,self.__metric_repository)

        stack_size = process_stack_usage.stack_size()

        self.assertEquals(stack_size, 136)

    def test_stack_referenced_size(self):
        self.skipTest(reason="Implement when suitable metric is found")

    def test_pid(self):
        process_stack_usage = ProcessStackUtil(1,self.__metric_repository)

        pid = process_stack_usage.pid()

        self.assertEqual(pid,1)

    def test_process_name(self):
        process_stack_usage = ProcessStackUtil(1,self.__metric_repository)

        name = process_stack_usage.process_name()

        self.assertEqual(name,'test')


    def test_user_id(self):
        process_stack_usage = ProcessStackUtil(1,self.__metric_repository)

        user_id = process_stack_usage.user_id()

        self.assertEqual(user_id,1)


if __name__ == '__main__':
    unittest.main()
