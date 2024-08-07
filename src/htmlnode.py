class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # tag - a string representing the HTML tag name
        self.tag = tag
        # value - a string representing the value of the HTML tag
        self.value = value
        # children - a list of HTMLNode objects representing the children of this node
        self.children = children
        # props - a dictionary of key-value pairs representing the attributes of the HTML tag.
        self.props = props

    # Give ourselves a way to print an HTMLNode object and see its tag, value, children, and props
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # return a string that represents the HTML attributes of the node
        if self.props is None:
            return ""

        key_value_pairs = []

        for key, value in self.props.items():
            key_value_pairs.append(f'{key}="{value}"')

        return " ".join(key_value_pairs)

# Child class of HTMLNode


class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        if value is None:
            raise ValueError("Value is a required attribute")
        super().__init__(tag, value, None, props)

    # Renders a leaf node as an HTML string (by returning a string)
    def to_html(self):
        if self.value is None:
            raise ValueError("Value is a requried attribute")
        if self.tag is None:
            return self.value

        # Otherwise render an HTML tag
        props_str = super().props_to_html()
        if props_str:
            return f'<{self.tag} {props_str}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):

    def __init__(self, children, tag, props=None):
        if not children:
            raise ValueError("Children is a required attribute")
        if tag is None:
            raise ValueError("Tag is a required attribute")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        # If the object doesn't have a tag raise a value Error
        if self.tag is None:
            raise ValueError("Tag is a required attribute")
        # If there are no children raise a value error
        if not self.children:
            raise ValueError("Children is a required attribute")

        # Return a string representing the HTML tag of the node and its children.
        # Recursive method -> each recursion is being called on a nested child
        # intialize empty string:
        html_str = ""
        for child in self.children:
            html_str += child.to_html()

        if html_str:
            return f'<{self.tag}>{html_str}</{self.tag}>'
