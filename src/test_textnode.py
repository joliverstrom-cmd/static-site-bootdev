import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noneq(self):
        node = TextNode("I am one", TextType.CODE)
        node2 = TextNode("I am another", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_noneq2(self):
        node = TextNode("I am one", TextType.CODE)
        node2 = TextNode("I am one", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("I am one", TextType.CODE, "www.kebab.se")
        node2 = TextNode("I am one", TextType.CODE, "www.kebab.se")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()