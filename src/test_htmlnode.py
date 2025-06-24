import unittest

from htmlnode import HTMLNode, LeafNode


#Add even more test cases (at least 3 in total) to check various edge cases, 
# like when the url property is None, 
# or when the text_type property is different. 
# You'll want to make sure that when properties are different, the TextNode objects are not equal.

class TestHtmlNode(unittest.TestCase):
    
    
    def test_emtpy(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
    
    def test_tag(self):
        test_tag = "tag-a"
        node = HTMLNode(test_tag)
        self.assertEqual(node.tag, test_tag)

    def test_value(self):
        test_value = "Lorem Ipsum"
        node = HTMLNode(None, test_value)
        self.assertEqual(node.value, test_value)

    def test_props(self):
        test_props = """{
    "href": "https://www.google.com",
    "target": "_blank",
}"""
        props_description = 'href="https://www.google.com" target="_blank"'

        node = HTMLNode(None, None, None, test_props)
        self.assertEqual(node.props_to_html(), props_description)
    
    def test_props_2(self):
        props = """{
    "asdf": "grsdf",
    "rhtjr": "rtjs6tjnf",
}"""
        props_description = 'asdf="grsdf" rhtjr="rtjs6tjnf"'

        node = HTMLNode(None, None, None, props)
        self.assertEqual(node.props_to_html(), props_description)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p2(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")


if __name__ == "__main__":
    unittest.main()
