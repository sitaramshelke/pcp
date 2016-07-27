import unittest
from mock import Mock
from pcp_mpstat import NoneHandlingPrinterDecorator

class TestNoneHandlingPrinterDecorator(unittest.TestCase):

    def test_print_report_without_none_values(self):
        printer = Mock()
        printer.Print = Mock()
        printer_decorator = NoneHandlingPrinterDecorator(printer.Print)

        printer_decorator.Print("2016-07-20 IST\tALL\t 1.23\t  2.34\t 3.45\t    4.56\t 5.67\t  6.78\t   7.89\t    8.9\t  1.34\t  2.45")

        printer.Print.assert_called_with("2016-07-20 IST\tALL\t 1.23\t  2.34\t 3.45\t    4.56\t 5.67\t  6.78\t   7.89\t    8.9\t  1.34\t  2.45")

    def test_print_report_with_none_values(self):
        printer = Mock()
        printer_decorator = NoneHandlingPrinterDecorator(printer.Print)

        printer_decorator.Print("2016-07-20 IST\tALL\t 1.23\t  None\t 3.45\t    4.56\t None\t  6.78\t   7.89\t    None\t  1.34\t  2.45")

        printer.Print.assert_called_with("2016-07-20 IST\tALL\t 1.23\t  ?\t 3.45\t    4.56\t ?\t  6.78\t   7.89\t    ?\t  1.34\t  2.45")

if __name__ == "__main__":
    unittest.main()
