class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None,):
        self.tag = tag if tag is not None else ''
        self.value = value if value is not None else {}
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")    
    
    def props_to_html(self,props):
        return ' '.join(f'{key}="{value}"' for key, value in props.items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    def add_child(self, child):
        self.children.append(child)

    def to_string(self):
        attr_str = ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())
        attr_str = f' {attr_str}' if attr_str else ''
        children_str = ''.join(child.to_string() if isinstance(child, HTMLNode) else str(child) for child in self.children)
        return f'<{self.tag}{attr_str}>{children_str}</{self.tag}>'