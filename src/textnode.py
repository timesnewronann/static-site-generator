from htmlnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def create_text_node(text_node):
    return LeafNode(text_node.text)


def create_bold_node(text_node):
    return LeafNode(text_node.text, "b")


def create_italic_node(text_node):
    return LeafNode(text_node.text, "i")


def create_code_node(text_node):
    return LeafNode(text_node.text, "code")


def create_link_node(text_node):
    if not hasattr(text_node, 'url'):
        raise ValueError("Link node is missing 'url' attribute")
    return LeafNode(text_node.text, "a", {"href": text_node.url})


def create_image_node(text_node):
    if not hasattr(text_node, 'url'):
        raise ValueError("Image node is missing 'url' attribute")
    return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})


def text_node_to_html_node(text_node):
    if text_node.text_type not in text_types:
        raise ValueError(f"Invalid text type: {text_node.text_type}")

    return text_types[text_node.text_type](text_node)


text_types = {
    "text": create_text_node,
    "bold": create_bold_node,
    "italic": create_italic_node,
    "code": create_code_node,
    "link": create_link_node,
    "image": create_image_node
}


text_node = TextNode("Hello, world!", "text", None)
bold_node = TextNode("Important", "bold", None)
link_node = TextNode("Click here", "link", url="https://example.com")

html_node = text_node_to_html_node(text_node)
print(html_node.to_html())
