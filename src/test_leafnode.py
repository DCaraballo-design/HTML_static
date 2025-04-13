import unittest
from src.htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_link(self):
        # Test for an anchor tag with href
        node = LeafNode(value="Click here", tag="a", props={"href": "https://www.example.com", "class": "link"})
        expected_html = '<a href="https://www.example.com" class="link">Click here</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_span(self):
        # Test for a span tag with a class
        node = LeafNode(value="Hello, World!", tag="span", props={"class": "highlight"})
        expected_html = '<span class="highlight">Hello, World!</span>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_plain_text(self):
        # Test for plain text (no tag)
        node = LeafNode(value="Just text")
        expected_html = "Just text"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_missing_value(self):
        # Test for missing value (should raise ValueError)
        with self.assertRaises(ValueError):
            LeafNode(value=None)

    def test_to_html_no_href_in_link(self):
        # Test for an anchor tag without href
        node = LeafNode(value="Broken link", tag="a")
        expected_html = "<a>Broken link</a>"
        self.assertEqual(node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()