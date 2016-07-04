import unittest
from mock import Mock
from pcp_pidstat import NoneHandlingPrinterDecorator
class TestNoneHandlingPrinterDecorator(unittest.TestCase):
    def setUp(self):
        self.options = Mock(
                        per_processor_usage = False,
                        show_process_user = None)

        process_1 = Mock(pid = Mock(return_value = 1),
                        process_name = Mock(return_value = "process_1"),
                        user_name = Mock(return_value='pcp'),
                        user_id = Mock(return_value=1000),
                        user_percent = Mock(return_value=2.43),
                        system_percent = Mock(return_value=1.24),
                        guest_percent = Mock(return_value=0.00),
                        total_percent = Mock(return_value=3.67),
                        cpu_number = Mock(return_value=1),)

        self.processes = [process_1]

    def test_print_report_without_none_values(self):
        printer = Mock()
        printer.Print = Mock()
        printer_decorator = NoneHandlingPrinterDecorator(printer)

        printer_decorator.Print("123\t1000\t1\t2.43\t1.24\t0.0\t3.67\t1\tprocess_1")

        printer.Print.assert_called_with("123\t1000\t1\t2.43\t1.24\t0.0\t3.67\t1\tprocess_1")

    def test_print_report_with_none_values(self):
        printer = Mock()
        printer.Print = Mock()
        printer_decorator = NoneHandlingPrinterDecorator(printer)

        printer_decorator.Print("123\t1000\t1\tNone\t1.24\t0.0\tNone\t1\tprocess_1")

        printer.Print.assert_called_with("123\t1000\t1\t?\t1.24\t0.0\t?\t1\tprocess_1")

if __name__ == "__main__":
    unittest.main()
