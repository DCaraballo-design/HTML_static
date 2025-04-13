class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if not self.props:
            return ""
        props_html = ""
        for prop, val in self.props.items():
            props_html += f' {prop}="{val}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        if value is None:
            raise ValueError("LeafNode requires a 'value' to be provided")
        super().__init__(tag=tag, value=value, children=None, props=props or {})
        if tag is None:
            self.tag = None

    def to_html(self):
        if self.tag == "a" and "href" in self.props:
            return f'<a href="{self.props["href"]}"{self.props_to_html()}>{self.value}</a>'
        elif self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

