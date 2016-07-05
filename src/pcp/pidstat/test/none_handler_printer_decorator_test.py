import unittest
from mock import Mock
from pcp_pidstat import NoneHandlingPrinterDecorator
class TestNoneHandlingPrinterDecorator(unittest.TestCase):
    
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
