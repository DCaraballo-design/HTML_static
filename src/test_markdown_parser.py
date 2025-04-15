import unittest
from markdown_parser import extract_title

class TestMarkdownParser(unittest.TestCase):
    def test_extract_title_valid(self):
        # Test with a valid H1 header
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_with_whitespace(self):
        # Test with extra whitespace around the title
        markdown = "#    Hello World    "
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_multiple_headers(self):
        # Test with multiple headers, ensuring the first H1 is returned
        markdown = "# First Title\n## Subheading\n# Second Title"
        self.assertEqual(extract_title(markdown), "First Title")

    def test_extract_title_no_h1(self):
        # Test with no H1 header, expecting a ValueError
        markdown = "## Subheading\nSome content here."
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_extract_title_empty_markdown(self):
        # Test with an empty markdown string, expecting a ValueError
        markdown = ""
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_extract_title_only_h1(self):
        # Test with only an H1 header and no other content
        markdown = "# TitleOnly"
        self.assertEqual(extract_title(markdown), "TitleOnly")

if __name__ == "__main__":
    unittest.main()