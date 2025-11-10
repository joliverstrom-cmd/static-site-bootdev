from blockparsing import *
from htmlnode import ParentNode
from textsplitting import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


def markdown_to_htmlnode(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        children.append(return_HTML_node(block))
    
    return ParentNode("div",children,None)


def return_HTML_node(block):
    match block_to_block_type(block):

        case BlockType.HEADING:
            return create_header_node(block)
        case BlockType.UL:
            return create_UL_block(block)
        case BlockType.OL:
            return create_OL_block(block)
        case BlockType.QUOTE:
            return create_quote_block(block)
        case BlockType.PARA:
            return create_paragraph_block(block)
        case BlockType.CODE:
            return create_code_block(block)



def create_header_node(block):
    headerlevel = len(re.findall("#{1,6} ",block)[0]) -1
    tag = f"h{headerlevel}"
    text = block[headerlevel+1:]

    children = text_to_children(text)
    return ParentNode(tag,children,None)

def create_UL_block(block):
    tag = "ul"
    
    ul_children = []
    lines = block.split("\n")
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        ul_children.append(ParentNode("li",children,None))

    return ParentNode(tag, ul_children,None)

def create_OL_block(block):
    tag = "ol"
    
    ol_children = []
    lines = block.split("\n")
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        ol_children.append(ParentNode("li",children,None))

    return ParentNode(tag, ol_children,None)

def create_quote_block(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def create_paragraph_block(block):
    tag = "p"
    text = block
    children = text_to_children(text)
    return ParentNode(tag,children,None)

def create_code_block(block):
    text = block[3:-3]
    text = text.lstrip()
    code_node = TextNode(text,TextType.CODE,None)
    code = text_node_to_html_node(code_node)

    return ParentNode("pre",[code],None)



def text_to_children(text):
    children = []

    text = text.replace("\n", " ")

    text_nodes = text_to_textnodes(text)
    
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    
    return children