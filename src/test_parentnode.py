import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    # test to_html
    def test_to_html(self):
        children = [
            LeafNode(tag="b", value="Bold text"),
            LeafNode(value="Normal text")
        ]
        node = ParentNode(children=children, tag="p")

        expected_html = "<p><b>Bold text</b>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    



