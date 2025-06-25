import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextType, TextNode

#Add even more test cases (at least 3 in total) to check various edge cases, 
# like when the url property is None, 
# or when the text_type property is different. 
# You'll want to make sure that when properties are different, the TextNode objects are not equal.
#def __init__(self, text = "", text_type = TextType.TEXT, url = None):
class TestSplitNodes(unittest.TestCase):
    def test_none_nodes(self):
        with self.assertRaises(SyntaxError):
            _ = split_nodes_delimiter(None, "`", TextType.CODE)
    
    def test_0_nodes(self):
        with self.assertRaises(SyntaxError):
            _ = split_nodes_delimiter([], "`", TextType.CODE)
    
    def test_1_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_2_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node_2 = TextNode("This is another text with a `same code block` word again", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node_2], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is another text with a ", TextType.TEXT),
            TextNode("same code block", TextType.CODE),
            TextNode(" word again", TextType.TEXT),
        ])

    def test_none_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        with self.assertRaises(SyntaxError):
            _ = split_nodes_delimiter([node], None, TextType.CODE)

    def test_empty_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        with self.assertRaises(SyntaxError):
            _ = split_nodes_delimiter([node], "", TextType.CODE)

    def test_delimiter_not_present(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "#", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a `code block` word", TextType.TEXT),
        ])

    def test_delimiter_not_balanced(self):
        node = TextNode("This is text with a `code block` `word", TextType.TEXT)
        with self.assertRaises(ValueError):
            _ = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_no_text_type(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        with self.assertRaises(SyntaxError):
            _ = split_nodes_delimiter([node], "`", None)

    def test_invalid_text_type(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        with self.assertRaises(SyntaxError):
            _ = split_nodes_delimiter([node], "`", "Invalid text type")

    def test_incorrect_text_type(self):
        node = TextNode("This is text with a `code block` word", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a `code block` word", TextType.CODE),
        ])

if __name__ == "__main__":
    unittest.main()
