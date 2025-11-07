from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    BOLD = "b"
    ITALIC = "i"
    TEXT = None
    CODE = "code"
    LINK = "a"
    IMAGE = "img"


class TextNode():
    
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url):
            return True
        return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    props = {}
    value = text_node.text

    valid_enums = [member.name for member in TextType]

    if text_node.text_type.name not in valid_enums:
        raise Exception("Not a valid text type")   

    if text_node.text_type == TextType.IMAGE:
        props["alt"] = text_node.text
        props["src"] = text_node.url
        value = ""

    if text_node.text_type == TextType.LINK:
        props["href"] = text_node.url
    
    leaf = LeafNode(text_node.text_type.value,value,props)

    return leaf
             




