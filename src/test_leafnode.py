import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafp(self):
        node1 = LeafNode("p", "hello hello")

        self.assertEqual(node1.to_html(),"<p>hello hello</p>")

    def test_none(self):
        node1 = LeafNode(None, "what is this",{"href": "http.123.abc", "action": "click"})

        self.assertEqual(node1.to_html(),"what is this")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click here",{"href": "www.test.123", "action": "click"})
        
        self.assertEqual(node.to_html(), '<a href="www.test.123" action="click">Click here</a>')


