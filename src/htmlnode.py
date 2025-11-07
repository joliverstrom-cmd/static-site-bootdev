

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        ret_string = ""
        if self.props:
            for key,value in self.props.items():
                ret_string += f' {key}="{value}"'
       
        return ret_string
    
    def __repr__(self):
        
        if self.children: 
            child_list = self.children.__repr__()
            return f"HTMLNode: {self.tag} - {self.value} - \n Children: {child_list} \n {self.props}"
        
        return f"HTMLNode: {self.tag} - {self.value} - No children - {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        
        if self.tag is None:
            raise ValueError("No tag found, this shouldn't be possible")
        
        if self.children is None:
            raise ValueError("No children associated with this parent, that shouldn't be possible")
        
        ret_string = ""
        for child in self.children:
            ret_string += child.to_html()
            #ret_string += child.to_html()
           

        return f"<{self.tag}{self.props_to_html()}>{ret_string}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        

        



