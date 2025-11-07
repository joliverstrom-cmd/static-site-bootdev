from enum import Enum
import re

class BlockType(Enum):
    PARA = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    LI = "ordered_list"

def block_to_block_type(block):

    if re.match("#{1,6} ",block):
        return BlockType.HEADING
    if block[0:3] == block[-3:] == "```":
        return BlockType.CODE
    
    lines = block.split("\n")
    
    if lines[0][0] == ">":
        quote = True
        for line in lines:
            if line[0] != ">":
                quote = False
                break
        if quote:
            return BlockType.QUOTE
    
    if lines[0][0:2] == "- ":
        ul = True
        for line in lines:
            if line[0:2] != "- ":
                ul = False
                break
        if ul:
            return BlockType.UL
    
    if re.match(r"\d\.",lines[0][0:2]):
        li = True
        dig = int(lines[0][0])
        
        for line in lines:
            if line[0:2] != f"{dig}.":
                li = False
                break
            dig += 1 
        if li:
            return BlockType.LI
        
    return BlockType.PARA
    
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(lambda x: x.strip(), blocks))
    
    blocks = list(filter(lambda x: len(x)>0,blocks))

    return blocks