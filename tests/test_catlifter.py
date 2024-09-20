from unittest import TestCase
from timberkat import TimberKat

class TestTimberKat(TestCase):

    def setUp(self) -> None:
        self.test_str = "hello world"

    def test_timberify(self):
        timberifier = TimberKat(self.test_str)
        timberified = timberifier.timberify()
        self.assertEqual(timberifier.base_text, self.test_str)
        self.assertEqual(timberified, self.test_str + 'timber')

    def test_untimberify(self):
        timberified = self.test_str + 'timber'
        timberified = TimberKat.untimberify(timberified)
        self.assertEqual(timberified.base_text, self.test_str)
