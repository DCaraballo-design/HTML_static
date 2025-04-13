import unittest
from src.htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_multiple_props(self):
        # Test for a tag with multiple properties
        node = LeafNode(value="Content", tag="div", props={"class": "container", "id": "main"})
        expected_html = '<div class="container" id="main">Content</div>'
    #    self.assertEqual(node.to_html(), expected_html)

    def test_to_html_empty_props(self):
        # Test for a tag with no properties
        node = LeafNode(value="Content", tag="p", props={})
        expected_html = "<p>Content</p>"
    #    self.assertEqual(node.to_html(), expected_html)

    #def test_to_html_no_props(self):
        # Test for a tag with props set to None
    #    node = LeafNode(value="Content", tag="p", props=None)
    #    expected_html = "<p>Content</p>"
    #    self.assertEqual(node.to_html(), expected_html)

    def test_to_html_no_tag(self):
        # Test for no tag (plain text output)
        node = LeafNode(value="Plain text")
        expected_html = "Plain text"
    #    self.assertEqual(node.to_html(), expected_html)

    def test_to_html_special_characters(self):
        # Test for special characters in value
        node = LeafNode(value="Special <>&\"'", tag="span")
        expected_html = '<span>Special <>&"\'</span>'
    #    self.assertEqual(node.to_html(), expected_html)

    def test_to_html_link_with_extra_props(self):
        # Test for an anchor tag with href and additional properties
        node = LeafNode(value="Visit", tag="a", props={"href": "https://example.com", "target": "_blank"})
        expected_html = '<a href="https://example.com" target="_blank">Visit</a>'
        self.assertEqual(node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()