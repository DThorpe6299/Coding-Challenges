from unittest import TestCase
from json_parser import json_parse
class JsonParserTestCase(TestCase):
    """Unit tests with sample test data."""

    def test_valid_json(self):
        # testing valid sample test data

        self.assertEqual(json_parse("./test/test/pass1.json"), ("Valid JSON Object:", 0))
        self.assertEqual(json_parse("./test/test/pass2.json"), ("Valid JSON Object:", 0))
        self.assertEqual(json_parse("./test/test/pass3.json"), ("Valid JSON Object:", 0))
    
    def test_invalid_json(self):
        # testing invalid sample test data

        self.assertEqual(json_parse("./test/test/fail1.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail2.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail3.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail4.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail5.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail6.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail7.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail8.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail9.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail10.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail11.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail12.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail13.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail14.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail15.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail16.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail17.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail18.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail19.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail20.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail21.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail22.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail23.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail24.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail25.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail26.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail27.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail28.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail29.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail30.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail31.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail32.json"), ("Invalid JSON Object", 1))
        self.assertEqual(json_parse("./test/test/fail33.json"), ("Invalid JSON Object", 1))