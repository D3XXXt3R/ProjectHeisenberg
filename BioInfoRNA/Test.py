from unittest import TestCase
from Helper import Helper


class TestHelper(TestCase):
    """
    test Helper
    """
    def test_characters_check(self):
        """
        test function characters_check
        """
        self.assertTrue(Helper.check_characters(self, "123456789"))
        self.assertTrue(Helper.check_characters(self, "CDNAAAPL"))
        self.assertTrue(Helper.check_characters(self, "...???@@@@@@@@@@"))
        self.assertTrue(Helper.check_characters(self, "&*#^#^#$#^#$^#^$#^#$"))
        self.assertIsNone(Helper.check_characters(self, "CCCCCCCCCCC"))
        self.assertIsNone(Helper.check_characters(self, "(((((("))
        self.assertIsNone(Helper.check_characters(self, "..........."))
        self.assertIsNone(Helper.check_characters(self, "CDNAAAAA"))

    def test_check_numbers(self):
        """
        test function check_numbers
        """
        self.assertTrue(Helper.check_numbers(self, "1214214124124"))
        self.assertTrue(Helper.check_numbers(self, "...................1"))
        self.assertTrue(Helper.check_numbers(self, "CDNAAAA9"))
        self.assertIsNone(Helper.check_numbers(self, ")))..)))"))
        self.assertIsNone(Helper.check_numbers(self, "(((...((("))
        self.assertIsNone(Helper.check_numbers(self, ".................."))

    def test_check_length(self):
        """
        test function check_length
        """
        self.assertTrue(Helper.check_length(self, "...."))
        self.assertTrue(Helper.check_length(self, "(((("))
        self.assertTrue(Helper.check_length(self, "CDN"))
        self.assertIsNone(Helper.check_length(self, ")))..)))"))
        self.assertIsNone(Helper.check_length(self, "(((...((("))
        self.assertIsNone(Helper.check_length(self, ".................."))

    def test_check_identity(self):
        """
        test function check_identity
        """
        self.assertTrue(Helper.check_identity(self, "(((...(((", 2, ["(((...(((", "(((...("]))
        self.assertTrue(Helper.check_identity(self, "CCCCC", 3, ["CCCCC", "CCCGGC", "CDAAA"]))
        self.assertTrue(Helper.check_identity(self, "(((.[[[[[[)))", 2, ["(((.[[[[[[)))", "CDNAAA"]))
        self.assertFalse(Helper.check_identity(self, "CDNAAA", 2, ["CCCCC", "CDNAAA"]))
        self.assertFalse(Helper.check_identity(self, ")))...)))", 3, ["((((((", ")))....(((", ")))...)))"]))
        self.assertFalse(Helper.check_identity(self, "(((.[[[[[[)))", 2, ["CCCCC", "CCCGGC"]))



