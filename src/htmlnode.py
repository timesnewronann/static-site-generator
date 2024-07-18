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
