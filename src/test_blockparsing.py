import unittest

from blockparsing import markdown_to_blocks, block_to_block_type, BlockType


class TestMD_To_Block(unittest.TestCase):

    def test_md_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            )
        
    def test_md_to_blocks_empty_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line





- This is a list
- with items




            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            )

class TestBlock_To_blocktype(unittest.TestCase):
    def test_header_block(self):
        block = """### This is a header block
                That can contain many lines"""
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )
    
    def test_code_block(self):
        block = """``` This is a code block
                That can contain many lines```"""
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )
    
    def test_quote_block(self):
        block = """>here's a quote
>and it goes on
>and on"""
        
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        )

    def test_unordered_list(self):
        block = """- here's a list
- and it goes on
- and on"""
        
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UL
        )

    def test_ordered_list(self):
        block = """1. here's a list
2. and it goes on
3. and on"""
        
        self.assertEqual(
            block_to_block_type(block),
            BlockType.OL
        )

    def test_wrong_ordered_list(self):
        block = """1. here's a list
3. and it goes on
4. and on"""
        
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARA
        )

    def empty_block(self):
        block = ""
       
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARA
        )
    
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UL)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OL)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)