import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "This is a text node", props={"href":"https://www.boot.dev"})
        self.assertEqual(
            "HTMLNode(p, This is a text node, href=https://www.boot.dev)", repr(node)
        )

    def test_tohtml(self):
        node = HTMLNode()  # Create an instance of the base class
        with self.assertRaises(NotImplementedError):
            node.to_html()  # Attempt to call to_html, which should raise the error

    def test_propstohtml(self):
        node = HTMLNode(props={"href":"https://www.google.com", "target":"_blank"})
        self.assertEqual(
            " href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html()
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

if __name__ == "__main__":
    unittest.main()