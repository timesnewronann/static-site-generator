import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    # focus on testing props_to_html
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.example.com"})
        self.assertEqual(node.props_to_html(),
                         'href="https://www.example.com"')

    # multiple props
    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a", props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),
                         'href="https://www.example.com" target="_blank"')

    def test_props_to_html_none(self):
        node = HTMLNode(tag="a")
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        child1 = HTMLNode(tag="li", value="Item 1")
        child2 = HTMLNode(tag="li", value="Item 2")
        node = HTMLNode("p", value="This is a paragraph.", children=[
                        child1, child2], props={"href": "https://www.example.com"})
        expected_repr = "HTMLNode(p, This is a paragraph., [HTMLNode(li, Item 1, None, None), HTMLNode(li, Item 2, None, None)], {'href': 'https://www.example.com'})"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
