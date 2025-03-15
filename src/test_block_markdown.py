import unittest
from block_markdown import *


class TestBlockMarkDown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type(self):
        # Heading tests - different levels
        assert block_to_block_type("# Heading 1") == BlockType.HEADING
        assert block_to_block_type("## Heading 2") == BlockType.HEADING
        assert block_to_block_type("###### Heading 6") == BlockType.HEADING
        
        # Code block tests
        assert block_to_block_type("```\nsome code\n```") == BlockType.CODE
        assert block_to_block_type("```\n```") == BlockType.CODE  # Empty code block
        
        # Quote tests
        assert block_to_block_type("> This is a quote") == BlockType.QUOTE
        assert block_to_block_type("> Line 1\n> Line 2") == BlockType.QUOTE
        
        # Unordered list tests
        assert block_to_block_type("- Item 1") == BlockType.ULIST
        assert block_to_block_type("- Item 1\n- Item 2") == BlockType.ULIST
        
        # Ordered list tests
        assert block_to_block_type("1. Item 1") == BlockType.OLIST
        assert block_to_block_type("1. Item 1\n2. Item 2") == BlockType.OLIST
        
        # Paragraph tests
        assert block_to_block_type("Just a normal paragraph") == BlockType.PARAGRAPH
        assert block_to_block_type("Line 1\nLine 2") == BlockType.PARAGRAPH
        
        # Edge cases
        assert block_to_block_type("#Not a heading") == BlockType.PARAGRAPH  # No space after #

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()