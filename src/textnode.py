class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


text_types = {
    "text": "text",
    "bold": "bold",
    "italic": "italic",
    "code": "code",
    "link": "link",
    "image": "image"
}


def text_node_to_html_node(text_node):
    if text_node.text_type not in text_types:
        raise ValueError(f"Invalid text type: {text_node.text_type}")

    # Now you can proceed with creating the appropriate HTMLNode
    # based on text_node.text_type
    """

    
    text_type_code: "code" tag, text
    text_type_link: "a" tag, anchor text, and "href" prop
    text_type_image: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
    """
    
    #text_type_text:
    if text_node.text_type == text_types["text"]:
        # This should become a LeafNode with no tag, just a raw text value.
        pass

    #text_type_bold: 
    if text_node.text_type == text_types["bold"]:
        #This should become a LeafNode with a "b" tag and the text
        pass

    #text_type_italic: "i" tag, text
    if text_node.text_type == text_types["italic"]:
        pass

    

    



        
