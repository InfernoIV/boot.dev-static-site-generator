import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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
    

    def test_split_nodes_image_none(self):
        with self.assertRaises(ValueError):
            _ = split_nodes_image(None)

    def test_split_nodes_image_empty(self):
        with self.assertRaises(ValueError):
            _ = split_nodes_image([])

    def test_split_nodes_image_incorrect(self):
        node = TextNode(None, TextType.TEXT)
        with self.assertRaises(ValueError):
            _ = split_nodes_image([node])

    def test_split_nodes_image_0(self):
        node = TextNode("This is text with no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [
                TextNode("This is text with no images", TextType.TEXT),
        ])

    def test_split_nodes_image_1(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and no other", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and no other", TextType.TEXT),
        ])

    def test_split_nodes_images_2(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ])

    def test_split_images_2_nodes(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node, node])
        self.assertListEqual(new_nodes, [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ])



    def test_split_link_none(self):
        with self.assertRaises(ValueError):
            _ = split_nodes_link(None)

    def test_split_link_empty(self):
        with self.assertRaises(ValueError):
            _ = split_nodes_link([])

    def test_split_link_incorrect(self):
        node = TextNode("", TextType.TEXT)
        with self.assertRaises(ValueError):
            _ = split_nodes_link([node])

    def test_split_link_0(self):
        node = TextNode("This is text with no links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [
                TextNode("This is text with no links", TextType.TEXT),
        ])
    
    def test_split_link_1(self):
        node = TextNode("This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and no other links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and no other links", TextType.TEXT),
        ])

    def test_split_link_2(self):
        node = TextNode("This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
        ])

    def test_split_link_2_nodes(self):
        node = TextNode("This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        new_nodes = split_nodes_link([node, node])
        self.assertListEqual(new_nodes, [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
        ])


if __name__ == "__main__":
    unittest.main()
