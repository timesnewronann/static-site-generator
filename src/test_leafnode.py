import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    # test to_html
    def test_to_html(self):
        node = LeafNode(value="This is a Leafnode", tag="a",
                        props={"href": "https://www.example.com"})
        expected_html = '<a href="https://www.example.com">This is a Leafnode</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_no_props(self):
        node = LeafNode(value="No props", tag="p")
        expected_html = '<p>No props</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_no_tag(self):
        node = LeafNode(value="No tag")
        expected_html = 'No tag'
        self.assertEqual(node.to_html(), expected_html)

    def test_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode(value=None, tag="p")


if __name__ == '__main__':
    unittest.main()
