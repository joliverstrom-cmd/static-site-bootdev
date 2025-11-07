import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_img(self):
        node = TextNode("This is an image", TextType.IMAGE, "www.picture.com/file.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "www.picture.com/file.png", "alt": "This is an image"},
        )

    def test_link_to_html(self):
        node = TextNode("Here's the link text", TextType.LINK, "www.picture.com/file.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Here's the link text")

    def test_code_to_html(self):
        node = TextNode("Some 1337 code", TextType.CODE, "www.picture.com/file.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Some 1337 code")

if __name__ == "__main__":
    unittest.main()