import unittest

from textnode import TextNode, TextType


#Add even more test cases (at least 3 in total) to check various edge cases, 
# like when the url property is None, 
# or when the text_type property is different. 
# You'll want to make sure that when properties are different, the TextNode objects are not equal.

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_emtpy(self):
        node = TextNode()
        node2 = TextNode()
        self.assertEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_type(self):
        node = TextNode("This is a text node")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
