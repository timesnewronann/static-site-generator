import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    # When the nodes are equal to each other
    def test_eq(self):
        node = TextNode("This is a text node", "bold",
                        "https://neetcode.io/practice")
        node2 = TextNode("This is a text node", "bold",
                         "https://neetcode.io/practice")

        self.assertEqual(node, node2)

    # When the nodes are not equal to each other
    def test_neq_different_properties(self):
        node3 = TextNode("This is a fart node", "loud",
                         "https://example.com")
        node4 = TextNode("This is a shart node",
                         "stinky", "https://example.com")

        self.assertNotEqual(node3, node4)

    def test_neq_null_url(self):
        node5 = TextNode("This is a text node", "bold", None)
        node6 = TextNode("This is a text node", "bold", "https://example.com")

        self.assertNotEqual(node5, node6)

    # When the node.url is equal to None
    def test_is_none_url(self):
        node7 = TextNode("This is a text node", "bold", None)

        self.assertIsNone(node7.url)

    def test_neq_different_text_type(self):
        node8 = TextNode(
            "This is a text node", "bold", "https://example.com")

        node9 = TextNode(
            "This is a text node", "italic", "https://example.com")

        self.assertNotEqual(node8.text_type, node9.text_type)


if __name__ == "__main__":
    unittest.main()
