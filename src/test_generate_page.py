import unittest

from generate_page import extract_title


class Test_Title_Extract(unittest.TestCase):

    def test_extract_title(self):
        md = """
# What a day
## Gorgeous
"""
        title = extract_title(md)
        print(title)
        self.assertEqual(title,"What a day")

    def test_no_title(self):
        md = """
## What a day
## Gorgeous
"""
        self.assertRaises(Exception,extract_title, md)

    
    def test_extract_title(self):
        md = """
## What a day
### Gorgeous
# Delicious dinner 
"""
        title = extract_title(md)
        print(title)
        self.assertEqual(title,"Delicious dinner")


