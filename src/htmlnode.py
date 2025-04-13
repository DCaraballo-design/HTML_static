class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        if value is None:
            raise ValueError("LeafNode requires a 'value' to be provided")
        # Call the parent class constructor with no children
        super().__init__(tag=tag, value=value, children=None, props=props or {})

    def to_html(self):
        # If the value is None, raise a ValueError
        if self.value is None:
            raise ValueError("LeafNode must have a value to render as HTML")

        # If the tag is None, return the value as raw text
        if self.tag is None:
            return self.value

        # Otherwise, render the HTML tag with props and value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

