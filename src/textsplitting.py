from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: TextNode, delimiter, text_type):
    return_nodes = []
    for node in old_nodes:
        
        if node.text_type is not TextType.TEXT:
            return_nodes.append(node)
            continue
        
        split_nodes = []
        text = node.text
        split = text.split(delimiter)
        if len(split) % 2 == 0:
            raise Exception("Invalid markdown, formatted section not closed")
        for i in range(len(split)):
            if split[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split[i],TextType.TEXT))
            else:
                split_nodes.append(TextNode(split[i],text_type))        
                                   
        return_nodes.extend(split_nodes)
    return return_nodes

def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

    return matches

def extract_markdown_link(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        image_tuples = extract_markdown_images(node.text)
        
        for tup in image_tuples:
            start_alt = text.index(tup[0])
            end_alt = start_alt + len(tup[0])  
            start_url = text.index(tup[1])
            end_url = start_url + len(tup[1])
            if (start_alt - 2) > 0:
                new_nodes.append(TextNode(text[:start_alt-2], TextType.TEXT))
            new_nodes.append(TextNode(tup[0],TextType.IMAGE,tup[1]))
            text = text[end_url+1:]

        if len(text) > 0:
            new_nodes.append(TextNode(text,TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        link_tuples = extract_markdown_link(node.text)
        
        for tup in link_tuples:
            start_alt = text.index(tup[0])
            end_alt = start_alt + len(tup[0])  
            start_url = text.index(tup[1])
            end_url = start_url + len(tup[1])
            if (start_alt-1) > 0:
                new_nodes.append(TextNode(text[:start_alt-1], TextType.TEXT))
            new_nodes.append(TextNode(tup[0],TextType.LINK,tup[1]))
            text = text[end_url+1:]

        if len(text) > 0:
            new_nodes.append(TextNode(text,TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    first_node = TextNode(text, TextType.TEXT)

    bold_nodes = split_nodes_delimiter([first_node],"**",TextType.BOLD)
    #print(bold_nodes)
    code_nodes = split_nodes_delimiter(bold_nodes,"`",TextType.CODE)
    #print(code_nodes)
    italic_nodes = split_nodes_delimiter(code_nodes,"_",TextType.ITALIC)
    #print(italic_nodes)
    img_nodes = split_nodes_image(italic_nodes)
    link_nodes = split_nodes_link(img_nodes)

    final_nodes = link_nodes

    return final_nodes