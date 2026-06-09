import io
import unittest
from contextlib import redirect_stdout

import coffee_machine_project as cm


class TestCoffeeMachineProject(unittest.TestCase):
    def setUp(self):
        self.original_resources = cm.resources.copy()

    def tearDown(self):
        cm.resources.clear()
        cm.resources.update(self.original_resources)

    def test_check_resource_sufficient_enough(self):
        self.assertTrue(cm.check_resource_sufficient("espresso"))

    def test_check_resource_sufficient_insufficient(self):
        cm.resources["water"] = 10
        self.assertFalse(cm.check_resource_sufficient("latte"))

    def test_check_money_sufficient_exact(self):
        cm.resources["money"] = 0
        ok, change = cm.check_money_sufficient("espresso", 6, 0, 0, 0)
        self.assertTrue(ok)
        self.assertEqual(change, 0.0)
        self.assertEqual(cm.resources["money"], 1.5)

    def test_check_money_sufficient_change(self):
        cm.resources["money"] = 0
        ok, change = cm.check_money_sufficient("latte", 11, 0, 0, 0)
        self.assertTrue(ok)
        self.assertEqual(change, 0.25)
        self.assertEqual(cm.resources["money"], 2.5)

    def test_check_money_sufficient_insufficient(self):
        cm.resources["money"] = 0
        ok, change = cm.check_money_sufficient("cappuccino", 10, 0, 0, 0)
        self.assertFalse(ok)
        self.assertEqual(change, 0.0)
        self.assertEqual(cm.resources["money"], 0)

    def test_make_coffee_reduces_resources(self):
        before = cm.resources.copy()
        cm.make_coffee("espresso")
        self.assertEqual(cm.resources["water"], before["water"] - 50)
        self.assertEqual(cm.resources["coffee"], before["coffee"] - 10)
        self.assertEqual(cm.resources["milk"], before["milk"])

    def test_generate_report_output(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            cm.generate_report()
        output = buffer.getvalue()
        self.assertIn("Water:", output)
        self.assertIn("Milk:", output)
        self.assertIn("Coffee:", output)
        self.assertIn("Money:", output)


if __name__ == "__main__":
    unittest.main()
