import unittest

from htmlnode import ParentNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_without_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError,parent_node.to_html)

    def test_to_html_with_grandchildren(self):      
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_many_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("h1", "child2")
        child_node3 = LeafNode("big", "child3")
        parent_node = ParentNode("div", [child_node, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><h1>child2</h1><big>child3</big></div>")

    def test_to_html_with_two_trees_of_grandchildren(self):      
        grandchild_node_1 = LeafNode("b", "grandchild 1")
        grandchild_node_2 = LeafNode("b", "grandchild 2")
        child_node_1 = ParentNode("span", [grandchild_node_1])
        child_node_2 = ParentNode("h1", [grandchild_node_2])
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild 1</b></span><h1><b>grandchild 2</b></h1></div>",
        )