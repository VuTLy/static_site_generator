
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        for key, value in self.props.items():
            result += f" {key}=\"{value}\""
        return result
    
    def __repr__(self):
        if self.props:
            props_str = " ".join([f"{k}={v}" for k, v in self.props.items()])
            return f"HTMLNode({self.tag}, {self.value}, {props_str})"
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        # Now handle the case where there IS a tag
        props_html = self.props_to_html() if self.props else ""
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, "", children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        props_html = self.props_to_html() if self.props else ""
        parent_tag = f"<{self.tag}{props_html}>"
        for children in self.children:
            parent_tag += children.to_html()
        return parent_tag + f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
