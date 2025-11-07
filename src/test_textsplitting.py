import unittest

from textsplitting import split_nodes_delimiter, extract_markdown_images, extract_markdown_link, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType


class TestTextSplitting(unittest.TestCase):
    def test_bold(self):
        oldnode = TextNode("What a **lovely** day",TextType.TEXT)
        new_nodes = split_nodes_delimiter([oldnode],"**",TextType.BOLD)

        self.assertEqual(new_nodes[0].text,"What a ")
        self.assertEqual(new_nodes[1].text,"lovely")
        self.assertTrue(new_nodes[1].text_type == TextType.BOLD)

    def test_code(self):
        oldnode = TextNode("Cool `coding` beats everything",TextType.TEXT)
        new_nodes = split_nodes_delimiter([oldnode],"`",TextType.CODE)

        self.assertEqual(new_nodes[2].text," beats everything")
        self.assertEqual(new_nodes[1].text,"coding")
        self.assertTrue(new_nodes[1].text_type == TextType.CODE)

    def test_nontext(self):
        oldnode = TextNode("Cool coding beats everything",TextType.CODE)
        new_nodes = split_nodes_delimiter([oldnode],"`",TextType.CODE)
        self.assertEqual(new_nodes[0].text,"Cool coding beats everything")

        self.assertTrue(new_nodes[0].text_type == TextType.CODE)

    def test_nonvalid_md(self):
        oldnode = TextNode("Cool `coding beats everything",TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter,[oldnode],"`",TextType.CODE)

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

class TestMDregex(unittest.TestCase):
    def test_extract_markdown_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
 
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_two_markdown_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![spanking image](www.123.se)"
        )
 
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),
                              ("spanking image", "www.123.se")], matches)
    
    def test_extract_two_links(self):
        matches = extract_markdown_link(
            "This is text with a [link](https://i.imgur.com) and another [spanking link](www.1337.se)"
        )
 
        self.assertListEqual([("link", "https://i.imgur.com"),
                              ("spanking link", "www.1337.se")], matches)
        
class TestImageSplit(unittest.TestCase):
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )
        
    def test_split_image_only_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
        [
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ],
        new_nodes,
    )
        
    def test_split_image_image_first(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and some text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
        [
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and some text", TextType.TEXT)
        ],
        new_nodes,
    )
        
    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com) and another [second link](aftonbladet.se)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://i.imgur.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "aftonbladet.se"
            ),
        ],
        new_nodes,
    )
        
    def test_split_only_link(self):
        node = TextNode(
            "[link](https://i.imgur.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
        [
            TextNode("link", TextType.LINK, "https://i.imgur.com"),
        ],
        new_nodes,
    )
        
    def test_split_link_with_something_after(self):
        node = TextNode(
            "[link](https://i.imgur.com) and some text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
        [
            TextNode("link", TextType.LINK, "https://i.imgur.com"),
            TextNode(" and some text", TextType.TEXT)
        ],
        new_nodes,
    )
        
        
class TestTextToTextnodes(unittest.TestCase):
    def test_string_with_all(self):
        nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        

    def test_string_with_two(self):
        nodes = text_to_textnodes("This is `code text` a ![cool image](https://i.imgur.com/123.jpeg)")
   
   