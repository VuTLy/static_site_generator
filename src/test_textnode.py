import unittest

from textnode import TextNode, TextType
from text_node_converter import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a link node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_with_url(self):
        node = TextNode("This is a link node", TextType.LINK, "www.boot.dev.com")
        expected_node = TextNode("This is a link node", TextType.LINK, "www.boot.dev.com")
        self.assertEqual(node, expected_node)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, normal, https://www.boot.dev)", repr(node)
        )

    #testing textnode convert to leafnode
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertEqual(html_node.props, None)  # Assuming no props for bold

    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertEqual(html_node.props, None)  # Assuming no props for italic

    def test_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")
        self.assertEqual(html_node.props, None)  # Assuming no props for code

    def test_link(self):
        node = TextNode("Link text", TextType.LINK, "www.boot-dev.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        self.assertEqual(html_node.props, {"href": "www.boot-dev.com"})  # Assuming no props for bold

    def test_image(self):
        # Assuming TextNode constructor takes text, type, and url/alt for image
        node = TextNode("Alt text", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")  # Empty string for images
        self.assertIsNotNone(html_node.props)
        self.assertEqual(html_node.props.get("src"), "https://example.com/image.png")
        self.assertEqual(html_node.props.get("alt"), "Alt text")

    def test_invalid(self):
        # Create a TextNode with an invalid type
        # This assumes you have a way to create an invalid type
        # You might need to adjust based on your actual implementation
        with self.assertRaises(Exception):  # Or a more specific exception
            node = TextNode("Invalid node", "INVALID_TYPE")  # Assuming string instead of enum creates invalid type
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()